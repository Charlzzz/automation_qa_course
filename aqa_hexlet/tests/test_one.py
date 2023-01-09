from selenium import webdriver
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

button_log = driver.find_element(By.XPATH, "//input[@id='login-button']").click()
print("Click")

text_title = driver.find_element(By.XPATH, "//span[@class='title']").text
# value_text = text_title.text

# assert text_title == "PRODUCTS", "Different words"
# print("Test done")



url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url

assert url == get_url




driver.close()
