import datetime
class Base():

    def __init__(self, driver):
        self.driver = driver

    """метод вызова урл"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """метод проверки слова приавторизации"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """метод скриншот"""
    def get_screenshot(self):
        new_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + new_data + ".png"
        self.driver.save_screenshot("C:\\Users\\WarMachine\\PycharmProjects\\main_project\\screen\\" + name_screenshot)

    """метод сравнения урл"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")