import requests
from datetime import datetime, timedelta
import os

# GitHub API configuration
GITHUB_API_URL = "https://api.github.com"
USERNAME = "davebecoding"  # Replace with your GitHub username
TOKEN = os.getenv("GITHUB_TOKEN") 

def get_repositories():
    url = f"{GITHUB_API_URL}/users/{USERNAME}/repos"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an error for bad responses
    return response.json()

def make_repo_private(repo_name):
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{repo_name}"
    headers = {
        "Authorization": f"token {TOKEN}"
    }
    data = {
        "private": True
    }
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()
    print(f"Repository '{repo_name}' is now private.")

def main():
    repos = get_repositories()
    one_year_ago = datetime.now() - timedelta(days=365)

    for repo in repos:
        repo_name = repo['name']
        created_at = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        
        # Check if the repo is older than one year and if it is public
        if created_at < one_year_ago and not repo['private']:
            print(f"Making repository '{repo_name}' private. Created at: {created_at}")
            make_repo_private(repo_name)

if __name__ == "__main__":
    main()

