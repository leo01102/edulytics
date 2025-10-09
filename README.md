# University Feedback System

An automated script that fetches student feedback from a Google Sheet, performs data analysis, generates personalized recommendations using OpenAI's API, and sends them to students via email.

## Core Functionality

- **Google Sheets Integration**: Pulls survey data directly from a specified Google Sheet.
- **Data Processing**: Utilizes Pandas to structure and process raw survey responses.
- **Rule-Based Analysis**: Generates initial recommendations based on predefined logic applied to quantitative feedback.
- **AI-Powered Analysis**: Leverages the OpenAI API for qualitative analysis of open-ended text responses.
- **Automated Email Dispatch**: Sends personalized feedback reports to students via SMTP.
- **Secure Configuration**: Manages all credentials and API keys through environment variables.

## System Workflow

The script executes the following workflow:

1.  **Fetch**: Authenticates with the Google API and retrieves all survey responses from the target spreadsheet.
2.  **Process**: Cleans and maps the raw data into a structured format for analysis.
3.  **Analyze**:
    - The `data_analysis_module` applies hard-coded rules to generate a baseline set of recommendations.
    - The `openai_module` forwards open-ended responses to the OpenAI API endpoint to generate deeper, context-aware conclusions.
4.  **Dispatch**: The `email_module` compiles the results from both analyses into a report and sends it to the corresponding student's email address.

## Tech Stack

- Python 3.8+
- Google API Client for Python
- Pandas & NumPy
- OpenAI Python Library
- python-dotenv

## Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the repository:**

```bash
git clone https://github.com/leo01102/university-feedback-system.git
cd university-feedback-system
```

**2. Create and activate a virtual environment:**

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Configure Google API Credentials:**

- Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
- Enable the **Google Sheets API**.
- Create credentials for an **OAuth client ID**, selecting **Desktop app** as the application type.
- Download the JSON file, rename it to `credentials.json`, and place it in the root directory of the project. This file is listed in `.gitignore` and should not be committed to version control.

**5. Set up environment variables:**

- Rename the `.env.example` file to `.env`.
- Populate the `.env` file with your credentials:

  ```dotenv
  # The ID of your Google Sheet, found in its URL
  SPREADSHEET_ID='YOUR_SPREADSHEET_ID_HERE'

  # Your API key from the OpenAI platform
  OPENAI_API_KEY='YOUR_OPENAI_API_KEY_HERE'

  # Gmail credentials for sending emails
  SMTP_SRU_USER='your-email@gmail.com'
  # An App Password generated from your Google Account settings
  SMTP_SRU_APPPASSWORD='YOUR_GOOGLE_APP_PASSWORD_HERE'
  ```

## Usage

The first time you run the script, a browser window will open to complete the Google OAuth2 flow. This will create a `token.json` file to store authentication tokens for subsequent runs.

To run the script, execute the main file:

```bash
python src/main.py
```

The script will then process all entries in the Google Sheet and send out emails accordingly.

## Project Structure

```
university-feedback-system/
│
├── src/
│   ├── __init__.py
│   ├── columnas_config.py
│   ├── data_analysis_module.py
│   ├── data_processing_module.py
│   ├── email_module.py
│   ├── main.py
│   ├── openai_module.py
│   ├── sheets_module.py
│   └── variables.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
