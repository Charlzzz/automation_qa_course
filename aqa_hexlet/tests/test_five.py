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

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
time.sleep(3)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()
# link_about.click()

url = "https://saucelabs.com/"
get_url = driver.current_url

assert url == get_url








