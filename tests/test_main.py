from app.utils import normalize_repo_name


def test_normalize_repo_name_with_url():
    repo_url = "https://github.com/mohak007/HTML.git"
    expected = "mohak007/HTML"

    assert normalize_repo_name(repo_url) == expected


def test_normalize_repo_name_with_repo_name():
    assert normalize_repo_name("mohak007/HTML") == "mohak007/HTML"
