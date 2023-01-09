import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

# from webdriver_manager.core import driver

driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
driver.get("https://www.saucedemo.com")
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")
password.send_keys(Keys.RETURN)

# menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
# time.sleep(3)
# link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()



price_product_one = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_one.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()


info_product_one = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = info_product_one.text
print(value_product_1)

info_product_one = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = info_product_one.text
print(value_product_1)



# url = "https://saucelabs.com/"
# get_url = driver.current_url
# assert url == get_url










