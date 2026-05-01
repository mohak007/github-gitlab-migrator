from github import Github
from app.config import GITHUB_TOKEN

class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)
    def get_repository(self, repo_name:str):
        return self.client.get_repo(repo_name) 
