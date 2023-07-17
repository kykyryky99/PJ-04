from pages.base_page import BasePage
from pages.locators import PassRecovery
from pages.locators import BaseLocators
import time, os


class PasswordRecoveryPage(BasePage):

    def __init__(self, driver, timeout=10):
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
        super().__init__(driver, url, timeout)

        self.open_start_page()

        time.sleep(3)
        self.phone = driver.find_element(*BaseLocators.PHONE)
        self.mail = driver.find_element(*BaseLocators.MAIL)
        self.username = driver.find_element(*BaseLocators.USERNAME)
        self.captcha = driver.find_element(*PassRecovery.PASSREC_CAPTCHA)
        self.button = driver.find_element(*PassRecovery.PASSREC_BUTTON_CONT)

    def choose_mail(self):
        self.mail.click()

    def choose_phone(self):
        self.phone.click()

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_captcha(self, value):
        self.captcha.send_keys(value)

    def press_reg_button(self):
        self.button.click()

