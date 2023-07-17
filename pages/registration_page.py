from pages.base_page import BasePage
from pages.locators import AuthLocators
from pages.locators import RegLocators
from pages.locators import BaseLocators


import time, os


class RegistrationPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, None, timeout)
        self.open_start_page()

        self.firstname = driver.find_element(*RegLocators.REG_FIRSTNAME)
        self.lastname = driver.find_element(*RegLocators.REG_LASTNAME)
        self.email = driver.find_element(*RegLocators.REG_EMAIL)
        self.reg_pass = driver.find_element(*BaseLocators.PASSWORD)
        self.reg_pass_confirm = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
        self.reg_button = driver.find_element(*RegLocators.REG_BUTTON)

    def open_start_page(self):
        self.driver.get(self.url)
        time.sleep(3)
        registration = self.driver.find_element(*AuthLocators.AUTH_REGISTER)
        registration.click()
        time.sleep(0.5)

    def enter_firstname(self, value):
        self.firstname.send_keys(value)

    def enter_lastname(self, value):
        self.lastname.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_reg_pass(self, value):
        self.reg_pass.send_keys(value)

    def enter_reg_pass_confirm(self, value):
        self.reg_pass_confirm.send_keys(value)

    def press_reg_button(self):
        self.reg_button.click()