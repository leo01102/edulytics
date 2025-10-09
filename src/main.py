# main.py

from sheets_module import get_credentials, fetch_sheet_data
from data_analysis_module import calculate_statistics, generate_recommendations
from openai_module import analyze_open_responses
from email_module import send_email
from data_processing_module import process_responses

def main():
    # --- AUTHENTICATION AND DATA FETCHING ---
    credentials = get_credentials()
    sheet_values = fetch_sheet_data(credentials)

    if not sheet_values:
        print("No data found in the sheet.")
        return

    # --- DATA PROCESSING AND ANALYSIS LOOP ---
    processed_responses = process_responses(sheet_values)

    for response in processed_responses:
        email = response['email']
        student_input_responses = response['student_input_responses']

        # generate recommendations using rule-based logic
        rule_based_recommendations = generate_recommendations(student_input_responses)

        # analyze open-ended responses with OpenAI
        ai_conclusion = analyze_open_responses(student_input_responses)

        # --- EMAIL COMPOSITION AND SENDING ---
        # combine both sets of recommendations into a single email body
        email_body = (
            "Rule-Based Recommendations\n\n"
            + "\n".join(f"- {rec}" for rec in rule_based_recommendations)
            + "\n\nAI-Powered Analysis\n\n"
            + ai_conclusion
        )
        
        print("\n--- Preparing to send email ---")
        print(f"To: {email}")
        print(f"Body:\n{email_body}")
        print("-----------------------------\n")

        # send the combined feedback via email
        send_email(email, "Personalized Academic Feedback", email_body)

if __name__ == "__main__":
    main()