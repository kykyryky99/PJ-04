import os
import time

from pages.base_page import BasePage
from pages.locators import AuthLocators
from pages.locators import BaseLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, None, timeout)
        self.open_start_page()

        time.sleep(3)

        self.username = driver.find_element(*BaseLocators.USERNAME)
        self.password = driver.find_element(*BaseLocators.PASSWORD)
        self.button_inter = driver.find_element(*AuthLocators.AUTH_BUTTON_ENTER)
        self.registration = driver.find_element(*AuthLocators.AUTH_REGISTER)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def button_inter(self):
        self.button_inter.click()

    def registration(self):
        self.registration.click()




