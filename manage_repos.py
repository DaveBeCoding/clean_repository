import requests
import os

# Fetch token and username
GTOKEN = os.getenv('GTOKEN')
GUSERNAME = os.getenv('GUSERNAME')

# Header, authentication
HEADERS = {
    'Authorization': f'token {GTOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repos():
    # Hit endpoint for user repositories
    url = f'https://api.github.com/users/{GUSERNAME}/repos'
    response = requests.get(url, headers=HEADERS)
    print(f"Response from get_repos: {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get repos: {response.status_code} {response.text}")
        return []

def archive_repo(repo_name):
    # Endpoint to update repository (set archived to true)
    url = f'https://api.github.com/repos/{GUSERNAME}/{repo_name}'
    response = requests.patch(url, headers=HEADERS, json={'archived': True})
    print(f"Response from archive_repo: {response.status_code} {response.json()}")
    if response.status_code == 200:
        print(f"Archived repository: {repo_name}")
    else:
        print(f"Failed to archive repository: {repo_name}")

def main():
    # Get list of repositories and archive each one
    repos = get_repos()
    for repo in repos:
        repo_name = repo['name']
        archive_repo(repo_name)

if __name__ == '__main__':
    main()
