from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GITLAB_URL = os.getenv("GITLAB_URL", "https://gitlab.com")

if not GITHUB_TOKEN:
    raise ValueError("Github_token is missing")
if not GITLAB_TOKEN:
    raise ValueError("GITLAB token is missing")
