def normalize_repo_name(repo_input: str) -> str:
    """Convert GitHub URL to owner/repo format."""
    if repo_input.startswith("https://github.com/"):
        repo_input = repo_input.replace("https://github.com/", "")

    if repo_input.endswith(".git"):
        repo_input = repo_input[:-4]

    return repo_input.strip()
