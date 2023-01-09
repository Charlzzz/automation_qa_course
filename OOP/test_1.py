import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_1():

    def test_select_product(self):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
        base_url = "https://www.saucedemo.com"
        driver.get(base_url)
        driver.maximize_window()
        print("Start Test_1")

        login = Login_page(driver)
        login.authorization(login_name="standard_user", login_password="secret_sauce")

        select_product = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Product add to cart")

        move_to_cart = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        move_to_cart.click()
        print("Move to the shopcart")

        success_title = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']"))).text
        assert success_title == "YOUR CART"

test = Test_1()
test.test_select_product()



