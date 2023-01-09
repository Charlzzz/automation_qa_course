from datetime import datetime

import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")


