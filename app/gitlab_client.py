import gitlab
from gitlab.exceptions import GitlabGetError
from app.config import GITLAB_TOKEN, GITLAB_URL


class GitLabClient:
    def __init__(self):
        self.client = gitlab.Gitlab(url=GITLAB_URL, private_token=GITLAB_TOKEN)
        self.client.auth()
        self.username = self.client.user.username

    def create_repository(self, repo_name: str):
        project_path = f"{self.username}/{repo_name}"

        print(f"Checking GitLab repository: {project_path}")

        try:
            project = self.client.projects.get(project_path)
            print(f"Repository '{repo_name}' already exists.")
            return project

        except GitlabGetError as e:
            if e.response_code != 404:
                raise

        print(f"Creating GitLab repository '{repo_name}'...")

        return self.client.projects.create({"name": repo_name, "visibility": "private"})
