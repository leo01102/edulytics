# openai_module.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# --- INITIALIZATION ---
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("Error: OPENAI_API_KEY not found in .env file. Please ensure it is set correctly.")

client = OpenAI(api_key=api_key)

def analyze_open_responses(student_responses):
    """
    Sends a student's open-ended responses to the OpenAI API to generate a summary and conclusion.
    """
    print("\nAnalyzing open-ended responses with OpenAI...")

    # construct a clear prompt for the language model
    prompt_text = "Based on the following student survey responses, provide helpful and constructive academic advice. " \
                  "Address whether they should consider another major, suggest suitable alternatives if applicable, " \
                  "and offer other useful conclusions. The advice should be encouraging and supportive.\n\n"
    
    # format the student's responses for clarity
    prompt_text += "Student Responses:\n" + "\n".join(f"- {res}" for res in student_responses if res) + "\n\n"
    prompt_text += "Provide your analysis and recommendations:"

    try:
        # call the OpenAI Chat Completions API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and empathetic academic advisor."
                },
                {
                    "role": "user",
                    "content": prompt_text
                }
            ],
            max_tokens=250,
            temperature=0.6
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error while getting conclusion from OpenAI: {e}"