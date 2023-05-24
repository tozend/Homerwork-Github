from selenium.webdriver.common.by import By


def test_login_negative_pom(github_ui):
    """
    This test checks if login page returns error message after login attempt with an incorrect username and password.
    """
    github_ui.open_login_page()
    github_ui.enter_credentials(username="non_existing_email@non_exist.com", password="wrongpassword123456")
    github_ui.click_submit_btn()

    assert github_ui.check_alert_message()


def test_login_negative_obsolete(web_driver):
    """
    This test checks if login page returns error message after login attempt with an incorrect username and password.
    """
    # Open login page
    web_driver.get("https://github.com/login")

    # Enter wrong email
    login_field = web_driver.find_element(By.ID, "login_field")
    login_field.send_keys("non_existing_email@non_exist.com")

    # Enter wrong password
    pass_field = web_driver.find_element(By.ID, "password")
    pass_field.send_keys("wrongpassword123456")

    # Click 'Sign in' button
    signin_button = web_driver.find_element(By.NAME, "commit")
    signin_button.click()

    # Error message validation
    error_msg = web_driver.find_element(By.CLASS_NAME, "js-flash-alert").text
    assert error_msg == "Incorrect username or password."
