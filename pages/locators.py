from selenium.webdriver.common.by import By


class BaseLocators:
    PHONE = (By.ID, "t-btn-tab-phone")
    MAIL = (By.ID, "t-btn-tab-mail")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    FORGOT_PASSWORD = (By.ID, "forgot_password")


class AuthLocators:
    AUTH_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_LS = (By.ID, "t-btn-tab-ls")
    AUTH_BUTTON_ENTER = (By.ID, "kc-login")
    AUTH_REGISTER = (By.ID, "kc-register")


class RegLocators:
    REG_FIRSTNAME = (By.NAME, "firstName")
    REG_LASTNAME = (By.NAME, "lastName")
    REG_REGION = (By.XPATH, '//input[@autocomplete="new-password"]')
    REG_EMAIL = (By.ID, "address")
    REG_PASS_CONFIRM = (By.ID, "password-confirm")
    REG_BUTTON = (By.NAME, "register")
    ERROR_SYMBOL = (By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')


class PassRecovery:
    PASSREC_CAPTCHA = (By.ID, "captcha")
    PASSREC_BUTTON_CONT = (By.ID, "reset")

