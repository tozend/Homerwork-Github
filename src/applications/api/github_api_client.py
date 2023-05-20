import requests

from src.config.config import Config


class GitHubAPIClient:
    """
    Class to represent API requests related to GitHub.com website
    """
    def login(self, username=Config.get_property('USERNAME'), password=Config.get_property('PASSWORD')):
        """
        Login with given credentials. If empty, the default ones from env_config will be used.
        """
        print(f'- - - LOGIN with credentials: {username}/{password} - - -')

    def logout(self):
        """
        Logout from environment
        """
        print('- - - LOGOUT - - -')

    def search_topics(self, topic_name):
        """
        Searches and returns repositories by given topic name

        Args:
            topic_name: Metadata used for searching repos (short_description, description, name, or display_name)

        Returns:
            List of repositories that matched given topic name.
        """
        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/search/topics",
            headers={
                "Accept": "applications/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            params={
                'q': str(topic_name)
            }
        )
        # Status code information
        print('Get Search Topic Response Status Code: ', r.status_code)

        # Throw an error if response is not 2xx or 3xx
        r.raise_for_status()

        # Return items from the body of response
        body = r.json()['items']
        return body
