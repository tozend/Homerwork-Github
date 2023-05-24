from selenium import webdriver
from selenium.webdriver.common.by import By


class GitHubApp:
    """
    Class to UI tests related to GitHub.com website
    """
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = None

    def launch_the_browser(self):
        """
        Launches selected browser. Raises exception if browser's webdriver is not supported.
        """
        match str(self.browser_name).lower():
            case "chrome":
                self.driver = webdriver.Chrome()
            case "firefox":
                self.driver = webdriver.Firefox()
            case _:
                raise Exception(f'Browser {self.browser_name} is not supported!')

    def _browser_launched_check(self):
        """
        Supporting method to checks if browser is actually launched first, before any further operations
        """
        if not self.driver:
            raise Exception("Method 'launch_the_browser' should be run first")

    def close_browser(self):
        """
        Closes the browser
        """
        self._browser_launched_check()
        self.driver.quit()

    def open_login_page(self):
        """
        Opens GitHub login page
        """
        self._browser_launched_check()
        self.driver.get("https://github.com/login")

    def enter_credentials(self, username, password):
        """
        Enter username and password credentials to fields founded on GitHub login page
        """
        self._browser_launched_check()
        login_field = self.driver.find_element(By.ID, "login_field")
        login_field.send_keys(username)

        pass_field = self.driver.find_element(By.ID, "password")
        pass_field.send_keys(password)

    def click_submit_btn(self):
        """
        Clicks 'Sign in' button on GitHub login page
        """
        self._browser_launched_check()
        signin_button = self.driver.find_element(By.NAME, "commit")
        signin_button.click()

    def check_alert_message(self):
        """
        Validates if error message (shown when wrong credentials are provided) is correct.

        Returns:
            True if shown error message is exactly as expected ("Incorrect username or password."), False otherwise
        """
        self._browser_launched_check()
        error_msg = self.driver.find_element(By.CLASS_NAME, "js-flash-alert").text
        return error_msg == "Incorrect username or password."
