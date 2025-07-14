import openai

def extract_tags(summary, openai_key):
    """
    Uses OpenAI to extract 5–8 concise topic tags from the podcast summary.

    Parameters:
        summary (str): The AI-generated summary text
        openai_key (str): OpenAI API key

    Returns:
        list[str]: Tags parsed as a list
    """
    openai.api_key = openai_key

    prompt = f"""Extract 5–8 concise topic tags from the following podcast summary. 
Format the output as a simple comma-separated list (no extra explanation):

{summary}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        tags_raw = response.choices[0].message["content"]
        tags = [tag.strip() for tag in tags_raw.split(",") if tag.strip()]
        return tags

    except Exception as e:
        print(f"❌ Tagging failed: {e}")
        return ["Tagging Error"]
