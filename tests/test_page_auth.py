from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


def test_mail_auth_page_success(open_browser):
    auth_page = AuthPage(open_browser)
    section_left = auth_page.driver.find_element(By.ID, "page-left")
    tag_with_logo = section_left.find_element(By.TAG_NAME, "h2")

    section_right = auth_page.driver.find_element(By.ID, "page-right")
    tag_with_login = section_right.find_element(By.TAG_NAME, "h1")

    assert tag_with_logo.text == "Личный кабинет"
    assert tag_with_login.text == "Авторизация"
