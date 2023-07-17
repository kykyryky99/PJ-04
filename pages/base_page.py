import os
from urllib.parse import urlparse

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver, url: str = None, timeout: int = 10):
        self.driver: WebDriver = driver
        self.driver.implicitly_wait(timeout)

        self.url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"

        if url is not None:
            self.url = url

    def open_start_page(self):
        self.driver.get(self.url)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
