import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    button_cont = "//input[@id='continue']"

    #Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_button_cont(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cont)))


    #Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("Input zip_code")

    def click_button_cont(self):
        self.get_button_cont().click()
        print("Click button continue")



    #Methods

    def input_information(self):
        self.get_current_url()
        self.input_first_name("ivan")
        self.input_last_name("Ivanov")
        self.input_zip_code("1233")
        self.click_button_cont()


















