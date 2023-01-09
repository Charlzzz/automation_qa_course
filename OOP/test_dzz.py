import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from login_page import Login_page


class Test_dz():

    def test_select_product(self):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
        base_url = "https://www.saucedemo.com"
        driver.get(base_url)
        driver.maximize_window()
        print("\nStart Test_1")

        login_list = ["standard_user", "problem_user", "locked_out_user", "performance_glitch_user"]
        login = Login_page(driver)
        for login_name in login_list:
            login.authorization(login_name)
            try:
                select_product = driver.find_element(By.XPATH, "//span[@class='title']").text
                exit_b = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
                exit_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']"))).click()
                assert select_product == "PRODUCTS"
                print("Test success")
                time.sleep(2)
            except :
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                print(f"oops error with {login_name}")

test = Test_dz()
test.test_select_product()
        # move_to_cart = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        # move_to_cart.click()







