import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    # url = "https://www.dns-shop.ru/"

    #Locators
    user_name = "//input[@autocomplete='username']"
    password = "//input[@autocomplete='current-password']"
    sign_in = "//div[@class='header-bottom__user-menu']"
    login_button = "//button[@class='base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"
    main_word = "//div[@class='user-profile__username']"
    btn_enter = "//button[@class='base-ui-button-v2_medium base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"
    enter_pass ="//div[@class='base-button-container base-button-container_blue']"
    coursor_word = "//div[@class='user-menu user-menu_logged']"




    #Getters

    # def get_button_enter_autform(self):
    #     return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.button_enter_autform)))

    def get_coursor_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.coursor_word)))


    def get_btn_enter(self):
        go_to_burg = self.driver.find_element(By.XPATH, self.btn_enter)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_enter)))
        # return ActionChains(self.driver).move_to_element(go_to_burg)

    def get_signin(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.sign_in)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))


    def get_enter_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_pass)))


    #Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_sign_in(self):
        self.get_signin().click()
        print("Click sign in")

    def click_btn_enter(self):
        self.get_btn_enter().click()

    def click_enter_pass(self):
        self.get_enter_pass().click()

    def move_on_acc(self):
        self.get_coursor_word().click()




    #Methods

    def authorization(self):
        self.get_current_url()
        time.sleep(1)
        self.click_sign_in()
        self.click_btn_enter()
        self.click_enter_pass()
        self.input_user_name("nts.sergei.test@mail.ru")
        self.input_password("helloworld")
        self.click_login_button()
        # time.sleep(1)
        self.move_on_acc()
        self.assert_word(self.get_main_word(), "Пришелец-OY74962")


















