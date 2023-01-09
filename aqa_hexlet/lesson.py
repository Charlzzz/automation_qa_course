from selenium import webdriver
from selenium.webdriver.common.by import By

# from webdriver_manager.core import driver

driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
driver.get("https://www.saucedemo.com")
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("looogin")
