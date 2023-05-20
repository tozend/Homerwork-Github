import os
import json


class Config:
    """
    Represents configuration for test environment, allows to retrieve info about prod/dev environment
    """
    DEFAULT_ENV = 'prod'

    @staticmethod
    def get_property(name):
        """
        Retrieves information from environment variables about target test environment.

        Args:
            name: Property name, key in .json file

        Returns:
            Value of given property name, value in .json file
        """
        # Define the environment - by default production env
        target = os.environ.get('TARGET', Config.DEFAULT_ENV)

        # Read target .json file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_config = os.path.join(current_dir, '..', '..', 'env_config', f'{target}.json')

        with open(path_to_config) as f:
            config_from_json = json.load(f)

        # Get the property name from given 'name' parameter
        value = config_from_json.get(name)

        return value
