import unittest

from allure_commons.types import AttachmentType
from selenium import webdriver

from AllVarsClass import AllVars
from Locators import Locators
from LoginPageClass import LoginPage
import allure
import pytest


@allure.story('Test interview - OrangeHRM')
@allure.feature('Test login')
# Base Class for the tests
class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=AllVars.CHROME_EXECUTABLE_PATH)
        self.driver.get(AllVars.BASE_URL)
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()


class Test_Login(BaseTest):
    def setUp(self):
        super().setUp()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Launch Login Page")
    def test_login_page_loaded_successfully(self):
        self.loginpage = LoginPage(self.driver)
        self.assertIn(AllVars.LOGIN_PAGE_TITLE, self.loginpage.driver.title)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Testing Login To Be Failed")
    def test_login_page_fail_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.failed_login()
        self.loginpage.assert_fail_login(Locators.LOGIN_MESSAGE, AllVars.ERROR_MESSAGE)
        allure.attach(self.driver.get_screenshot_as_png(), name='UnsuccessfulLoginScreen'
                      , attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Testing Login To Be Successful")
    def test_login_page_success_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.successful_login()
        self.loginpage.assert_success_login(Locators.LOGIN_WELCOME)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Get User's Name in Welcome")
    def test_login_page_success_get_name(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.successful_login()
        if self.loginpage.assert_success_login(Locators.LOGIN_WELCOME):
            name = self.loginpage.get_name()
            self.assertTrue(True, 'username is {}'.format(name))
        else:
            self.assertFalse(True, 'Login Was Not Successful')