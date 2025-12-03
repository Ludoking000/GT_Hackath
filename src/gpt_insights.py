from openai import OpenAI

# Create client
client = OpenAI()

def generate_gpt_summary(text_insights):
    """
    Uses GPT-4o-mini (or GPT-4o) to generate a polished, executive-level summary.
    This converts raw numerical insights into a readable narrative.

    Requirements:
    - OPENAI_API_KEY must be set in your environment.
    """

    prompt = f"""
    You are a Senior Marketing Analyst. You will read raw KPI insights and write a 
    professional executive summary.

    RAW INSIGHTS:
    {text_insights}

    TASK:
    Write a clear 2–3 paragraph business summary that includes:
    - What is happening overall in the marketing performance
    - Major improvements and declines
    - Key risks or opportunities
    - 2–3 actionable recommendations for next steps

    Tone:
    - Professional
    - Concise
    - Business-oriented
    - No emojis
    """

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )
        return response.output_text

    except Exception as e:
        print("⚠️ GPT Error:", e)
        return (
            "Executive Summary unavailable (API Error).\n"
            "However, the system remains fully functional."
        )
