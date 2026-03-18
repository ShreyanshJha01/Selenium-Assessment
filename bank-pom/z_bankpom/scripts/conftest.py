import time
import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()
