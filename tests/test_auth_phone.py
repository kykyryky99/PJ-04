from pages.auth_page import AuthPage
from pages.data import Data
import time


def test_phone_auth_page_success(open_browser):
    auth_page = AuthPage(open_browser)
    time.sleep(3)
    auth_page.enter_username(Data.PHONE_VALID)
    auth_page.enter_password(Data.PASS_VALID)
    auth_page.button_inter.click()

    assert auth_page.get_relative_link() == "/account_b2c/page", "login error"
    time.sleep(5)


def test_phone_auth_page_error(open_browser):
    auth_page = AuthPage(open_browser)
    time.sleep(3)
    auth_page.enter_username(Data.PHONE_VALID)
    auth_page.enter_password(Data.PASS_NO_VALID)
    auth_page.button_inter.click()

    assert auth_page.get_relative_link() != "/account_b2c/page", "login success"

    time.sleep(5)