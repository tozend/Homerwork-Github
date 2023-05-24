import pytest
from selenium import webdriver

from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config
from src.applications.ui.github_app import GitHubApp


@pytest.fixture(scope='module')
def fixture_github_api_client():
    """
    Initial setup for GitHub API Client.
    Creates new object of GitHubAPIClient class, login to environment,
    returns api object from fixture and finally logout user.
    """
    api = GitHubAPIClient()
    api.login(username=Config.get_property("USERNAME"), password=Config.get_property("PASSWORD"))

    yield api

    api.logout()


@pytest.fixture
def web_driver():
    """
    Simple version of fixture for tests.
    Opens Chrome browser, returns webdriver object, quits browser.
    """
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def github_ui():
    """
    Fixture for GitHub UI tests.
    Opens selected browser, returns GitHubApp object, quits browser.
    """
    github_app = GitHubApp(browser_name="chrome")
    github_app.launch_the_browser()

    yield github_app

    github_app.close_browser()
