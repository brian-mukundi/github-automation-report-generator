GitHub Automation Report Generator

A Python automation tool that fetches GitHub user data using the GitHub API, generates a structured report, and sends the report via email using the SendGrid API.

This project demonstrates real-world backend automation including API integration, CLI tooling, environment configuration, and external scheduling.

---

Overview

This system automatically generates GitHub performance reports for a user and delivers them via email.

The script can be run manually from the terminal or scheduled using external schedulers such as Windows Task Scheduler or cron jobs.

This makes it suitable for real-world automation workflows.

---

Features

• Fetches GitHub user data using the GitHub API
• Generates structured GitHub performance reports
• Sends reports via email using SendGrid API
• Command Line Interface (CLI) support
• Environment variable configuration for security
• Designed for external automation scheduling
• Modular Python architecture

---

Technologies Used

- Python 3
- Requests Library
- Python Dotenv
- GitHub API
- SendGrid Email API
- Command Line Interface (argparse)

---

Project Structure

github-automation-report-generator/
│
├── main.py
├── github_service.py
├── report_generator.py
├── email_service.py
├── config.py
├── .env.example
├── requirements.txt
└── README.md

---

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/github-automation-report-generator.git

Navigate into the project:

cd github-automation-report-generator

Install dependencies:

pip install -r requirements.txt

---

Configuration Setup

This project uses environment variables to store sensitive credentials.

Create a ".env" file in the project root.

Example configuration:

GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_email@example.com
TO_EMAIL=recipient_email@example.com

Important:

Replace all placeholder values with your own credentials.

Never commit your real ".env" file to GitHub.

---

CLI Usage

The system includes a command-line interface.

Example usage:

python main.py --username octocat

Example with email sending enabled:

python main.py --username octocat --send

---

Example Output

GitHub Weekly Report

Username: octocat
Followers: 9300
Following: 9
Public Repositories: 8
Account Age: 5000 days

Strong project activity detected.

---

Automating the Script

The project does not use a Python scheduling library.

Instead, it is designed to be scheduled externally.

Example automation tools:

• Windows Task Scheduler
• Cron Jobs (Linux / macOS)

---

Windows Task Scheduler Example

1. Open Task Scheduler
2. Click Create Basic Task
3. Set trigger to Weekly
4. Choose Start a Program
5. Program/script:

python

6. Add arguments:

path\to\main.py --username octocat --send

Now the report will run automatically on schedule.

---

Future Improvements

Possible upgrades:

• HTML email reports
• Repository analytics reports
• Multiple user reporting
• Logging system
• Docker container support
• Web dashboard interface

# github-automation-report-generator
