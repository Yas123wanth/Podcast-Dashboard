import openai

def summarize_transcript(transcript_url):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize and extract key topics from the following transcript."},
            {"role": "user", "content": f"Transcript file URL: {transcript_url}"}
        ]
    )
    return response.choices[0].message["content"]
