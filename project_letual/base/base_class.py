import datetime

import allure


class Base:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    """метод открытия"""
    def open(self):
        self.driver.get(self.url)

    """метод вызова урл"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """метод проверки слова приавторизации"""
    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result



    """метод скриншот"""
    @allure.feature("Take screenshot")
    def get_screenshot(self):
        new_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + new_data + ".png"
        self.driver.save_screenshot("C:\\Users\\WarMachine\\PycharmProjects\\project_ziel\\screen\\" + name_screenshot)

    """метод сравнения урл"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    def assert_url_in(self, result):
        get_url = self.driver.current_url
        assert  result in get_url
        print("Good value URL")