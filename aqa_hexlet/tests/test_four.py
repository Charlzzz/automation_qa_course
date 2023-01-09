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

# now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
# screenn = "aqa" + now_date + ".png"
# driver.save_screenshot(screenn)
# driver.execute_script("window.scrollTo(0, 200)")

action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//footer[@class='footer']")
action.move_to_element(red_t_shirt).perform()

time.sleep(3)








