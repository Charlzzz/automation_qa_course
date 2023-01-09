import allure

from pages.header_page import Header_page


@allure.feature("Headers sections")
class TestHeadersSections:
    @allure.title("Section Actions")
    def test_section_actions(self, driver):
        section_actions = Header_page(driver, "https://www.dns-shop.ru/")
        section_actions.open()
        section_actions.click_headers_actions()
        result_word = section_actions.get_word_actions().text
        assert result_word == "Акции"

    @allure.title("Section Shops")
    def test_sections_shops(self, driver):
        section_shops = Header_page(driver, "https://www.dns-shop.ru/")
        section_shops.open()
        checking_url = "https://www.dns-shop.ru/shops/"
        section_shops.click_headers_shops()
        section_shops.assert_url_in(checking_url)














