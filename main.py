import argparse
from github_service import fetch_github_data
from report_generator import generate_report
from email_service import send_email
from config import GITHUB_USERNAME


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--send", action="store_true",
                        help="Send email report")
    args = parser.parse_args()

    data = fetch_github_data()
    report = generate_report(data, GITHUB_USERNAME)

    print(report)

    if args.send:
        send_email(report)
        print("Email sent.")


if __name__ == "__main__":
    main()
