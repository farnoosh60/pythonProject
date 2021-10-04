from selenium.webdriver.common.by import By


class Locators():
    # --- Login Page Locators ---
    LOGIN_USERNAME = (By.ID, "txtUsername")
    LOGIN_PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    LOGIN_MESSAGE = (By.XPATH, "//span[@id='spanMessage']")

    LOGIN_DEFAULT_USERNAME = (By.XPATH, "//div[@id='content']/div[2]/span")
    LOGIN_WELCOME = (By.ID, "welcome")

