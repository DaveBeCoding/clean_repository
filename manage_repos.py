import requests
import os
from datetime import datetime, timedelta

# Fetch GitHub token and username from environment variables
GTOKEN = os.getenv('GTOKEN')
GUSERNAME = os.getenv('GUSERNAME')

# Set up headers for authentication
HEADERS = {
    'Authorization': f'token {GTOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repos():
    # API endpoint to list user repositories
    url = f'https://api.github.com/users/{GUSERNAME}/repos'
    response = requests.get(url, headers=HEADERS)
    print(f"Response from get_repos: {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get repos: {response.status_code} {response.text}")
        return []

def is_repo_inactive_for_a_year(repo):
    # Get the current date and the date one year ago
    one_year_ago = datetime.now() - timedelta(days=365)
    # Parse the pushed_at date from the repository
    last_push_date = datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
    # Check if the last push date is older than one year ago
    return last_push_date < one_year_ago

def archive_repo(repo_name):
    # API endpoint to update repository (set archived to true)
    url = f'https://api.github.com/repos/{GUSERNAME}/{repo_name}'
    response = requests.patch(url, headers=HEADERS, json={'archived': True})
    print(f"Response from archive_repo: {response.status_code} {response.json()}")
    if response.status_code == 200:
        print(f"Archived repository: {repo_name}")
    else:
        print(f"Failed to archive repository: {repo_name}")

def main():
    # Get list of repositories and archive each one that is inactive for a year
    repos = get_repos()
    for repo in repos:
        if is_repo_inactive_for_a_year(repo):
            repo_name = repo['name']
            archive_repo(repo_name)

if __name__ == '__main__':
    main()
