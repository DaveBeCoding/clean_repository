import requests
import os

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GTOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_repos():
    url = f"{GITHUB_API_URL}/user/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Response from get_repos: {response.status_code}")
        print(response.json())
        return []

def archive_repo(repo):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo['name']}"
    data = {"archived": True}
    response = requests.patch(url, headers=headers, json=data)
    print(f"Response from archive_repo: {response.status_code} {response.json()}")
    if response.status_code == 200:
        print(f"Archived repository: {repo['name']}")

def main():
    repos = get_repos()
    if isinstance(repos, list):
        print(f"Type of repos: {type(repos)}")
        print(f"Repos content: {repos}")
        for repo in repos:
            if not repo['private']:  # Process only public repositories
                archive_repo(repo)
    else:
        print("Failed to retrieve repositories")

if __name__ == "__main__":
    main()
