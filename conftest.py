import pytest

from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config


@pytest.fixture(scope='module')
def fixture_github_api_client():
    """
    Initial setup for GitHub API Client.
    Creates new object of GitHubAPIClient class, login to environment,
    returns api object from fixture and finally logout user.
    """
    api = GitHubAPIClient()
    api.login(username=Config.get_property("LOGIN"), password=Config.get_property("PASSWORD"))

    yield api

    api.logout()
