import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def open_browser() -> WebDriver:
    service = Service(executable_path=r"..\chromedriver.exe")
    driver: WebDriver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()
