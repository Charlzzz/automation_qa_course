import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators




    #Getters








    #Actions






    #Methods

    def finish(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()





















