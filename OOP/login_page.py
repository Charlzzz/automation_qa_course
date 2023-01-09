import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name,login_password="secret_sauce"):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Input login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(login_password)



        password.send_keys(Keys.RETURN)
        print("Input password")



















