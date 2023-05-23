from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_negative():
    # Created a driver
    driver = webdriver.Chrome()

    # Open login page
    driver.get("https://github.com/login")

    # Enter wrong email
    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys("non_existing_email@non_exist.com")

    # Enter wrong password
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys("wrongpassword123456")

    # Click 'Sign in' button
    signin_button = driver.find_element(By.NAME, "commit")
    signin_button.click()

    # Error message validation
    error_msg = driver.find_element(By.CLASS_NAME, "js-flash-alert").text
    assert error_msg == "Incorrect username or password."

    driver.quit()
