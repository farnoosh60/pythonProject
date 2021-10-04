from BasePageClass import BasePage
from AllVarsClass import AllVars
from Locators import Locators


class LoginPage(BasePage):
    """Login Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(AllVars.BASE_URL)

    def failed_login(self):
        sheet = super().read_file()
        username = super().get_username(sheet, 0, 2)
        password = super().get_password(sheet, 1, 2)
        self.login(username, password)

    def successful_login(self):
        # read from the login page
        username_password = self.get_text(Locators.LOGIN_DEFAULT_USERNAME)
        user_pass_array = self.split(username_password)
        username = user_pass_array[2]
        password = user_pass_array[4]
        self.login(username, password)

    def login(self, username, password):
        self.enter_text(Locators.LOGIN_PASSWORD, password)
        self.enter_text(Locators.LOGIN_USERNAME, username)
        self.click(Locators.LOGIN_BUTTON)

    def get_name(self):
        welcome_message = self.get_text(Locators.LOGIN_WELCOME)
        user = self.split(welcome_message)
        print(user[1])
        return user[1]