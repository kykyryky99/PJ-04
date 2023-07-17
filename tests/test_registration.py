from pages.data import Data
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By


def test_registration(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_VALID)
    reg_page.enter_lastname(Data.LAST_NAME_VALID)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.ID, "page-right")
    tag_p_with_email = section.find_element(By.TAG_NAME, "p")

    assert tag_p_with_email.text == f"Kод подтверждения отправлен на адрес {email}", "registration error"


def test_registration_1_letter_name(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_1)
    reg_page.enter_lastname(Data.LAST_NAME_1)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", "registration error"

def test_registration_2_letter_name(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_2)
    reg_page.enter_lastname(Data.LAST_NAME_2)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()


    section = reg_page.driver.find_element(By.ID, "page-right")
    tag_p_with_email = section.find_element(By.TAG_NAME, "p")

    assert tag_p_with_email.text == f"Kод подтверждения отправлен на адрес {email}", "registration error"


def test_registration_30_letter_name(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_30)
    reg_page.enter_lastname(Data.LAST_NAME_30)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()


    section = reg_page.driver.find_element(By.ID, "page-right")
    tag_p_with_email = section.find_element(By.TAG_NAME, "p")

    assert tag_p_with_email.text == f"Kод подтверждения отправлен на адрес {email}", "registration error"

def test_registration_31_letter_name(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_31)
    reg_page.enter_lastname(Data.LAST_NAME_31)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", "registration error"

def test_registration_no_valid_email(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_NO_VALID

    reg_page.enter_firstname(Data.FIRST_NAME_VALID)
    reg_page.enter_lastname(Data.LAST_NAME_VALID)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", "registration error"


def test_registration_no_valid_phone(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.PHONE_NO_VALID

    reg_page.enter_firstname(Data.FIRST_NAME_VALID)
    reg_page.enter_lastname(Data.LAST_NAME_VALID)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.REG_PASS_VALID)
    reg_page.enter_reg_pass_confirm(Data.REG_PASS_VALID)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", "registration error"


def test_registration_cyrillic_password(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_VALID)
    reg_page.enter_lastname(Data.LAST_NAME_VALID)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.PASS_CYRILLIC)
    reg_page.enter_reg_pass_confirm(Data.PASS_CYRILLIC)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Пароль должен содержать только латинские буквы", "registration error"

def test_registration_numbers_password(open_browser):
    reg_page = RegistrationPage(open_browser)
    email = Data.MAIL_VALID_RANDOM

    reg_page.enter_firstname(Data.FIRST_NAME_VALID)
    reg_page.enter_lastname(Data.LAST_NAME_VALID)
    reg_page.enter_email(email)
    reg_page.enter_reg_pass(Data.PASS_NUMBERS)
    reg_page.enter_reg_pass_confirm(Data.PASS_NUMBERS)
    reg_page.press_reg_button()

    section = reg_page.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    assert section.text == "Длина пароля должна быть не менее 8 символов", "registration error"


