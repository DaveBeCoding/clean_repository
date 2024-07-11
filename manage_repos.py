import requests
import os

def get_repos(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repos: {response.status_code}")
        return []

def archive_repo(repo, token):
    url = f"https://api.github.com/repos/{repo['full_name']}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"archived": True}
    response = requests.patch(url, headers=headers, json=data)
    return response.status_code, response.json()

def main():
    username = os.getenv("GITHUB_USERNAME")
    token = os.getenv("GTOKEN")

    repos = get_repos(username, token)
    print(f"Response from get_repos: {len(repos)}")
    print(f"Type of repos: {type(repos)}")
    print(f"Repos content: {repos}")

    for repo in repos:
        if not repo['private']:
            status_code, response_content = archive_repo(repo, token)
            print(f"Response from archive_repo: {status_code} {response_content}")
            if status_code == 200:
                print(f"Archived repository: {repo['name']}")
            else:
                print(f"Failed to archive repository: {repo['name']} with status {status_code}")

if __name__ == "__main__":
    main()
