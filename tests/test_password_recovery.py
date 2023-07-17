from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.data import Data

from pages.password_recovery_page import PasswordRecoveryPage


def test_password_recovery_phone(open_browser):
    pas_rec = PasswordRecoveryPage(open_browser)

    pas_rec.choose_phone()
    pas_rec.enter_username(Data.PHONE_VALID)
    pas_rec.enter_captcha(Data.CAPTCHA_NO_VALID)
    pas_rec.press_reg_button()

    try:
        pas_rec.driver.find_element(By.ID, "form-error-message")
    except NoSuchElementException:
        raise AssertionError("recovery error")


def test_password_recovery_mail(open_browser):
    pas_rec = PasswordRecoveryPage(open_browser)

    pas_rec.choose_mail()
    pas_rec.enter_username(Data.MAIL_VALID)
    pas_rec.enter_captcha(Data.CAPTCHA_NO_VALID)
    pas_rec.press_reg_button()

    try:
        pas_rec.driver.find_element(By.ID, "form-error-message")
    except NoSuchElementException:
        raise AssertionError("recovery error")