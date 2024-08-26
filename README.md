# Assignment Reminder Bot

A Python script that automatically sends daily email reminders for upcoming assignments based on the due dates provided in a spreadsheet. This bot runs every morning at 9 AM on the cloud to help you stay organized throughout the school year. The cloud used for this project is called PythonAnywhere; The API which processes the spreadsheet is Sheety.

**Spreadsheet:**
<img width="400" alt="Screenshot 2024-08-26 at 5 00 09 PM" src="https://github.com/user-attachments/assets/58d954c2-b581-4b9f-8e65-95f6b9f22bab">


## Features

- Parses a spreadsheet containing class names, assignment names, due dates, and times.
- Sends email reminders using the SMTP library.
- Automatically runs on the cloud every day at 9 AM.
- Keeps you on track with assignment deadlines.

## Getting Started

### Prerequisites

- Python 3.x
- An email account with SMTP access (e.g., Gmail, Outlook)
- `smtplib` Python library (included in the standard library)
- Create a PythonAnywhere account
- Create a Sheety Account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/assignment-reminder-bot.git
   cd assignment-reminder-bot

2. Install required libraries (if any):
   
   ```bash
   pip install -r requirements.txt

3. Create a spreadsheet that includes class names, assignments, due dates, and times (respectively).

4. Create a Sheety Account, start a new project, and link the spreadsheet to the project.
   - Enable the 'GET' requests in order to obtain the spreadsheet information.
   - Copy the provided endpoint and incorporate it into the script as your 'url.'

6. Configure your email settings in the script:

   EMAIL_ADDRESS = "your_email@example.com"
   
   EMAIL_PASSWORD = "your_email_password"
   
   SMTP_SERVER = "smtp.example.com"
   
   SMTP_PORT = 587

8. Set up the script to run daily at a specified time using a cloud service or a task scheduler, like PythonAnywhere.


**Running the Script:**
To run the script locally:
  ```bash
python main.py





   
   
