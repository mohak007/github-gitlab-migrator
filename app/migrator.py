import os
import shutil
from git import Repo, GitCommandError
from app.config import GITLAB_TOKEN


class RepositoryMigrator:
    def migrate(self, github_url: str, gitlab_url: str):
        repo_name = github_url.split("/")[-1].replace(".git", "")

        if os.path.exists(repo_name):
            shutil.rmtree(repo_name)

        print("Cloning repository from GitHub...")
        repo = Repo.clone_from(github_url, repo_name)

        authenticated_url = gitlab_url.replace(
            "https://",
            f"https://oauth2:{GITLAB_TOKEN}@"
        )

        print("Adding GitLab remote...")

        if "gitlab" in [remote.name for remote in repo.remotes]:
            repo.delete_remote("gitlab")

        gitlab_remote = repo.create_remote(
            "gitlab",
            authenticated_url
        )

        try:
            print("Pushing branches...")
            gitlab_remote.push(
                refspec="refs/heads/*:refs/heads/*",
                force=True
            )

            print("Pushing tags...")
            gitlab_remote.push(
                refspec="refs/tags/*:refs/tags/*",
                force=True
            )

            print("Migration completed successfully!")

        except GitCommandError as e:
            print(f"Migration failed: {e}")
            raise
