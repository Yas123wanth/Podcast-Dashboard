import streamlit as st
import time
from modules.s3_upload import upload_to_s3
from modules.transcribe import transcribe_audio_job
from modules.summarize import summarize_transcript
from modules.emailer import send_summary_email


# 🔐 Load secrets
aws_key = st.secrets["aws"]["access_key"]
aws_secret = st.secrets["aws"]["secret_key"]
region = st.secrets["aws"]["region"]
openai_key = st.secrets["openai"]["api_key"]

sender = st.secrets["email"]["sender"]
recipient = st.secrets["email"]["recipient"]
email_password = st.secrets["email"]["password"]

# 🛡️ Validate secrets
if not all([aws_key, aws_secret, region, openai_key, sender, recipient, email_password]):
    st.warning("⚠️ One or more secrets are missing. Please check `.streamlit/secrets.toml`.")
    st.stop()

# 🎧 UI Setup
st.title("🎙️ Podcast Dashboard")
st.write("Upload → Transcribe → Summarize → Email & Download")

# 📤 File Upload
uploaded_file = st.file_uploader("Upload podcast audio", type=["mp3", "wav"])

if uploaded_file:
    filename = uploaded_file.name
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"✅ Saved `{filename}` locally")

    st.audio(uploaded_file, format="audio/mp3")
    media_format = filename.split(".")[-1]
    object_name = f"audio/{filename}"
    bucket = "sagemaker-ap-south-1-427640063444"

    # 📡 Upload to S3
    media_uri = upload_to_s3(filename, bucket, object_name, aws_key, aws_secret, region)
    if media_uri:
        st.success(f"📤 Uploaded to S3: `{media_uri}`")
    else:
        st.error("❌ Upload failed.")
        st.stop()

    # 🎙️ Transcribe
    job_name = f"job-{int(time.time())}"
    transcript_url = transcribe_audio(media_uri, media_format, job_name, aws_key, aws_secret, region)

    if transcript_url:
        st.success("✅ Transcription completed")
        st.markdown(f"[View Transcript JSON]({transcript_url})")

        # 🧠 Summarize
        summary = summarize_transcript(transcript_url, openai_key)
        st.subheader("🧠 AI-Generated Summary")
        st.write(summary)

        from modules.tagger import extract_tags

        tags = extract_tags(summary, openai_key)
        st.markdown("🏷️ **Auto-Extracted Tags:**")
        st.write(tags)


        # 📥 Download summary
        st.download_button("📥 Download Summary", summary, file_name="podcast_summary.txt")

        # 📧 Optional Email
        if st.checkbox("📬 Send summary via email"):
            email_status = send_summary_email(sender, recipient, email_password, summary)
            st.info(email_status)
    else:
        st.error("❌ Transcription failed. Please verify S3 access and format.")
