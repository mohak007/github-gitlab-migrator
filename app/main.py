from app.github_client import GitHubClient
from app.gitlab_client import GitLabClient
from app.migrator import RepositoryMigrator


def normalize_repo_name(repo_input: str) -> str:
    repo_input = repo_input.strip()

    if repo_input.startswith("https://github.com/"):
        repo_input = repo_input.replace("https://github.com/", "")

    if repo_input.endswith(".git"):
        repo_input = repo_input[:-4]

    return repo_input


def migrate_single_repo():
    github_client = GitHubClient()
    gitlab_client = GitLabClient()
    migrator = RepositoryMigrator()

    repo_input = input("Enter GitHub repository (URL or owner/repo): ")

    repo_name = normalize_repo_name(repo_input)

    github_repo = github_client.get_repository(repo_name)

    print(f"Found GitHub repository: {github_repo.full_name}")

    gitlab_project = gitlab_client.create_repository(github_repo.name)

    migrator.migrate(github_repo.clone_url, gitlab_project.http_url_to_repo)


def migrate_all_repositories():
    github_client = GitHubClient()
    gitlab_client = GitLabClient()
    migrator = RepositoryMigrator()

    repos = github_client.get_user_repositories()

    migrated = 0
    failed = 0

    for repo in repos:
        try:
            print(f"\nMigrating: {repo.full_name}")

            gitlab_project = gitlab_client.create_repository(repo.name)

            migrator.migrate(repo.clone_url, gitlab_project.http_url_to_repo)

            migrated += 1

        except Exception as e:
            print(f"Failed: {repo.full_name} -> {e}")
            failed += 1

    print("\nMigration Summary")
    print("-" * 30)
    print(f"Successful: {migrated}")
    print(f"Failed: {failed}")


def main():
    print("\nGitHub to GitLab Migrator")
    print("1. Migrate single repository")
    print("2. Migrate all repositories")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        migrate_single_repo()
    elif choice == "2":
        migrate_all_repositories()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
