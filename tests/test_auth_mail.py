from pages.auth_page import AuthPage
from pages.data import Data


def test_mail_auth_page_success(open_browser):
    auth_page = AuthPage(open_browser)
    auth_page.enter_username(Data.MAIL_VALID)
    auth_page.enter_password(Data.PASS_VALID)
    auth_page.button_inter.click()

    assert auth_page.get_relative_link() == "/account_b2c/page", "login error"


def test_mail_auth_page_error(open_browser):
    auth_page = AuthPage(open_browser)
    auth_page.enter_username(Data.MAIL_VALID)
    auth_page.enter_password(Data.PASS_NO_VALID)
    auth_page.button_inter.click()

    assert auth_page.get_relative_link() != "/account_b2c/page", "login success"
