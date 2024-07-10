import requests
import datetime
import os

# class GitHubManager:
#     def __init__(self, token, username):
#         self.token = token
#         self.username = username
#         self.headers = {
#             'Authorization': f'token {self.token}',
#             'Accept': 'application/vnd.github.v3+json'
#         }

#     def get_repos(self):
#         response = requests.get(f'https://api.github.com/users/{self.username}/repos', headers=self.headers)
#         return response.json()

#     def archive_repo(self, repo_name):
#         url = f'https://api.github.com/repos/{self.username}/{repo_name}'
#         response = requests.patch(url, headers=self.headers, json={'archived': True})
#         return response.status_code == 200

#     def transfer_repo(self, repo_name, new_owner):
#         url = f'https://api.github.com/repos/{self.username}/{repo_name}/transfer'
#         response = requests.post(url, headers=self.headers, json={'new_owner': new_owner})
#         return response.status_code == 202

#     def add_topics(self, repo_name, topics):
#         url = f'https://api.github.com/repos/{self.username}/{repo_name}/topics'
#         response = requests.put(url, headers={
#             **self.headers,
#             'Accept': 'application/vnd.github.mercy-preview+json'
#         }, json={'names': topics})
#         return response.status_code == 200

#     def list_topics(self, repo_name):
#         url = f'https://api.github.com/repos/{self.username}/{repo_name}/topics'
#         response = requests.get(url, headers={
#             **self.headers,
#             'Accept': 'application/vnd.github.mercy-preview+json'
#         })
#         return response.json()

# def main():
#     token = os.getenv('GITHUB_TOKEN')
#     username = os.getenv('GITHUB_USER')
#     manager = GitHubManager(token, username)

#     # Example usage: Archiving repositories older than a year
#     repos = manager.get_repos()
#     cutoff_date = datetime.datetime.now() - datetime.timedelta(days=365)
#     for repo in repos:
#         repo_name = repo['name']
#         last_updated = datetime.datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
#         if last_updated < cutoff_date:
#             manager.archive_repo(repo_name)
#             print(f'Archived repository: {repo_name}')

# if __name__ == "__main__":
#     main()

import requests
import datetime
import os

class GitHubManager:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_repos(self):
        response = requests.get(f'https://api.github.com/users/{self.username}/repos', headers=self.headers)
        print("Response from get_repos:", response.status_code)
        print("Response content:", response.content)  # Print raw response content for debugging
        return response.json()

    def archive_repo(self, repo_name):
        url = f'https://api.github.com/repos/{self.username}/{repo_name}'
        response = requests.patch(url, headers=self.headers, json={'archived': True})
        print("Response from archive_repo:", response.status_code, response.json())
        return response.status_code == 200

    def transfer_repo(self, repo_name, new_owner):
        url = f'https://api.github.com/repos/{self.username}/{repo_name}/transfer'
        response = requests.post(url, headers=self.headers, json={'new_owner': new_owner})
        print("Response from transfer_repo:", response.status_code, response.json())
        return response.status_code == 202

    def add_topics(self, repo_name, topics):
        url = f'https://api.github.com/repos/{self.username}/{repo_name}/topics'
        response = requests.put(url, headers={
            **self.headers,
            'Accept': 'application/vnd.github.mercy-preview+json'
        }, json={'names': topics})
        print("Response from add_topics:", response.status_code, response.json())
        return response.status_code == 200

    def list_topics(self, repo_name):
        url = f'https://api.github.com/repos/{self.username}/{repo_name}/topics'
        response = requests.get(url, headers={
            **self.headers,
            'Accept': 'application/vnd.github.mercy-preview+json'
        })
        print("Response from list_topics:", response.status_code, response.json())
        return response.json()

def main():
    token = os.getenv('GITHUB_TOKEN')
    username = os.getenv('GITHUB_USERNAME')
    manager = GitHubManager(token, username)

    # Example usage: Archiving repositories older than a year
    repos = manager.get_repos()
    print("Type of repos:", type(repos))  # Debugging print statement
    print("Repos content:", repos)  # Debugging print statement
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=365)
    for repo in repos:
        repo_name = repo['name']
        last_updated = datetime.datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
        if last_updated < cutoff_date:
            manager.archive_repo(repo_name)
            print(f'Archived repository: {repo_name}')

if __name__ == "__main__":
    main()

