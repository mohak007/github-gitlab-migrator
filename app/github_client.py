from github import Github
from app.config import GITHUB_TOKEN


class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)
        self.user = self.client.get_user()

    def get_repository(self, repo_name: str):
        return self.client.get_repo(repo_name)

    def get_user_repositories(self):
        """
        Return only repositories owned by the authenticated user.
        Excludes organization repositories, forks, and archived repos.
        """
        repositories = []

        for repo in self.user.get_repos():
            if (
                repo.owner.login == self.user.login
                and not repo.fork
                and not repo.archived
            ):
                repositories.append(repo)

        return repositories
