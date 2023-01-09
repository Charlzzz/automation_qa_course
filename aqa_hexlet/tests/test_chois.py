
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By



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

print("Выберите товар из списка:\n1.Sauce Labs Backpack\n2.Sauce Labs Bolt T-Shirt\n"
      "3.Sauce Labs Onesie\n4.Sauce Labs Bike Light\n5.Sauce Labs Fleece Jacket\n6.Test.allTheThings() T-Shirt (Red)")

your_choice = input("Ваш выбор: ")

dirb_products = {
                    "1": "Sauce Labs Backpack",
                    "2": "Sauce Labs Bolt T-Shirt",
                    "3": "Sauce Labs Onesie",
                    "4": "Sauce Labs Bike Light",
                    "5": "Sauce Labs Fleece Jacket",
                    "6": "Test.allTheThings() T-Shirt (Red)"
}
dirb_links = {
                    "Sauce Labs Backpack": "//*[@id='item_4_title_link']/div",
                    "Sauce Labs Bolt T-Shirt": "//*[@id='item_1_title_link']/div",
                    "Sauce Labs Onesie": "//*[@id='item_2_title_link']/div",
                    "Sauce Labs Bike Light": "//*[@id='item_0_title_link']/div",
                    "Sauce Labs Fleece Jacket": "//*[@id='item_5_title_link']/div",
                    "Test.allTheThings() T-Shirt (Red)": "//*[@id='item_3_title_link']/div"
}

'''save products title'''
f_product = dirb_products[your_choice]
print(f"First product title: {f_product}")



move_product_cart = driver.find_element(By.XPATH, dirb_products[f_product])
move_product_cart.click()
'''save products price'''
product_one_price = driver.find_element(By.XPATH, "//button[class='btn btn_primary btn_small btn_inventory']/div/div/div[2]/div[3]").text
print(f"First product price: {product_one_price}")


'''add products to the cart'''
product_one_to_cart = driver.find_element(By.CSS_SELECTOR, "#btn_small btn_inventory").click()

print(f"Add first product to the cart: {f_product}")


time.sleep(3)

'''move to the cart'''
shopping_cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

'''move to the form'''
btn_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()

'''filling form'''
f_name = driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("vova")
l_name = driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("ivanov")
zip_name = driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("111222")

'''apply form'''
btn_continue = driver.find_element(By.XPATH, "//input[@id='continue']").click()

'''save products price cart'''
first_price_to_cart = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
second_price_to_cart = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
print(f"First product price to the cart: {first_price_to_cart}")
print(f"Second product price to the cart: {second_price_to_cart}")

'''save total product'''
total_product_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]").text
print(f"Total price: {total_product_price}")




assert str(59.98) in total_product_price
assert product_one_price == first_price_to_cart
assert product_two_price == second_price_to_cart

'''submit finish'''
btn_finish = driver.find_element(By.XPATH, "//button[@id='finish']").click()
















