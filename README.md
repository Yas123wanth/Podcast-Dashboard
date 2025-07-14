 🎙️ Podcast Dashboard

An intelligent audio summarization platform that transcribes podcast episodes using AWS Transcribe, generates concise summaries with OpenAI, 
extracts semantic tags, and optionally delivers the result via email. Built with Streamlit for an interactive UI and modular Python architecture for scalability.


🔧 Features

📤 Upload `.mp3` or `.wav` podcast audio files
🧾 Transcribe audio using **AWS Transcribe**
🧠 Summarize content via **OpenAI GPT-3.5**
🏷️ Extract contextual topic tags
📬 Email summary to predefined recipients
📥 Download summary as `.txt`
☁️ S3-based dynamic file upload
🧩 Modular Python structure for maintainability

🧠 Tech Stack

| Component         | Tech Used                      |
|-------------------|--------------------------------|
| UI Framework      | `Streamlit`                    |
| Cloud Storage     | `Amazon S3`                    |
| Speech-to-Text    | `AWS Transcribe`               |
| NLP & Summarization | `OpenAI GPT-3.5`             |
| Email Delivery    | `SMTP` + `smtplib`             |
| Environment Mgmt  | `secrets.toml` via Streamlit   |


🗂️ Project Structure

podcast-dashboard/ 
├── app.py # Streamlit UI logic
├── requirements.txt 
├── README.md 
   ├── modules/ │ 
      ├── s3_upload.py # Upload to S3 │
      ├── transcribe.py # Transcription job logic │
      ├── summarize.py # GPT summarization │ 
      ├── tagger.py # Topic tag extraction │ 
      └── emailer.py # Email integration 
  └── .streamlit/ 
  ├── config.toml # Theming 
  └── secrets.toml (excluded from repo) # API keys



🚀 Deploy Your Own (Free Hosting)

- Streamlit Community Cloud: https://streamlit.io/cloud  
- Push your code to a public GitHub repo  
- Add secrets in cloud console (not in repo!)


 🔐 Required Secrets Format (`secrets.toml`)

```toml
aws.access_key = "YOUR_AWS_ACCESS_KEY"
aws.secret_key = "YOUR_AWS_SECRET_KEY"
aws.region = "YOUR_REGION"

openai.api_key = "YOUR_OPENAI_API_KEY"

email.sender = "you@example.com"
email.recipient = "team@example.com"
email.password = "your_app_password"
```

🧪 Run Locally
pip install -r requirements.txt
streamlit run app.py
