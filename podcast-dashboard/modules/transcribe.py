import boto3, time

def transcribe_audio_job(media_uri, media_format, job_name, aws_key, aws_secret, region):
    transcribe = boto3.client("transcribe", aws_access_key_id=aws_key, aws_secret_access_key=aws_secret, region_name=region)
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": media_uri},
        MediaFormat=media_format,
        LanguageCode="en-US"
    )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        state = status["TranscriptionJob"]["TranscriptionJobStatus"]
        if state in ["COMPLETED", "FAILED"]:
            break
        time.sleep(5)

    if state == "COMPLETED":
        return status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
    else:
        return None
