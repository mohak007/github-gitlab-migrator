from app.github_client import GitHubClient
from app.gitlab_client import GitLabClient
from app.migrator import RepositoryMigrator


def normalize_repo_name(repo_input: str) -> str:
    repo_input = repo_input.strip()

    if repo_input.startswith("https://github.com/"):
        repo_input = repo_input.replace(
            "https://github.com/",
            ""
        )

    if repo_input.endswith(".git"):
        repo_input = repo_input[:-4]

    return repo_input


def main():
    repo_input = input(
        "Enter GitHub repository (URL or owner/repo): "
    )

    github_repo_name = normalize_repo_name(repo_input)

    github_client = GitHubClient()
    gitlab_client = GitLabClient()
    migrator = RepositoryMigrator()

    github_repo = github_client.get_repository(
        github_repo_name
    )

    print(f"Found GitHub repository: {github_repo.full_name}")

    gitlab_project = gitlab_client.create_repository(
        github_repo.name
    )

    print(f"Created GitLab repository: {gitlab_project.name}")

    migrator.migrate(
        github_repo.clone_url,
        gitlab_project.http_url_to_repo
    )


if __name__ == "__main__":
    main()
