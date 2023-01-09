from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Header_page(Base):

    #locators
    headers_actions = "//*[@class='header-top-menu__common-list']/li[2]"
    word_actions = "//h1[@class='actions-page__title']"
    headers_shops = "//*[@class='header-top-menu__common-list']/li[3]"
    # word_shops =


    # Getters
    def get_headers_actions(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.headers_actions)))

    def get_word_actions(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.word_actions)))

    def get_headers_shops(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.headers_shops)))


    # Actions
    def click_headers_actions(self):
        self.get_headers_actions().click()
        print("Move to section Actions")

    def click_headers_shops(self):
        self.get_headers_shops().click()
        print("Move to section Shops")
