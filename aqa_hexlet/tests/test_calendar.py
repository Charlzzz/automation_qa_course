import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


'''заходим на сайт'''
driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

'''чистим  поле'''
new_date = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
new_date.click()
new_date.send_keys(Keys.BACKSPACE * 10)

'''находим дату на сегодня'''
now_date = datetime.datetime.utcnow().strftime("%d")

'''вводим дату + 10 дней'''
new_date.send_keys(f"{int(now_date) + 10}/17/2022")
time.sleep(3)
new_date.send_keys(Keys.RETURN)

