from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import xlrd
import re

import AllVarsClass


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def navigate_to():
        driver = webdriver.Chrome(executable_path=AllVarsClass.CHROME_EXECUTABLE_PATH)
        driver.get(AllVarsClass.BASE_URL)

    def read_file(self):
        workbook = xlrd.open_workbook("DataFile.xls")
        return workbook.sheet_by_name("login")

    def get_username(self, sheet, cell_x, cell_y):
        username = sheet.cell_value(cell_y, cell_x)
        return username

    def get_password(self, sheet, cell_x, cell_y):
        password = sheet.cell_value(cell_y, cell_x)
        return password

    # this function asserts successful or failed login.
    def assert_success_login(self, by_locator):
        # try except block
        try:
            # identify element
            web_element = self.driver.find_element_by_id("welcome")
            welcome_text = web_element.text
            print("Element exist -" + welcome_text)
            return True
        # NoSuchElementException thrown if not present
        except NoSuchElementException:
            print("Element does not exist")
            assert False

    def assert_fail_login(self, by_locator, error_message):
        web_element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == error_message

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def click(self, by_locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).click()

    @staticmethod
    def split(txt_to_split):
        return re.split(r'\W+', txt_to_split)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).text
