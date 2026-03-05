from datetime import datetime


def generate_report(data, username):
    followers = data.get("followers", 0)
    following = data.get("following", 0)
    public_repos = data.get("public_repos", 0)
    created_at = data.get("created_at")

    account_age = "Unknown"

    if created_at:
        created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        days_active = (datetime.utcnow() - created_date).days
        account_age = f"{days_active} days"

    report = f"""
GitHub Weekly Report

Username: {username}
Followers: {followers}
Following: {following}
Public Repositories: {public_repos}
Account Age: {account_age}
"""

    if public_repos > 5:
        report += "\nStrong project activity detected.\n"

    return report
