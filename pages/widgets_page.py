import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SortablePageLocators, ResizablePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            "first": {"title": self.locators.SECTION_FIRST,
                      "content": self.locators.SECTION_CONTENT_FIRST},
            "second": {"title": self.locators.SECTION_SECOND,
                       "content": self.locators.SECTION_CONTENT_SECOND},
            "third": {"title": self.locators.SECTION_THIRD,
                      "content": self.locators.SECTION_CONTENT_THIRD}
        }
        section_title = self.element_is_visible(accordian[accordian_num]["title"])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]["content"]).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]["content"]).text

        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, "2020")
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute("value")
        return value_date_before, value_date_after



    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slide_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute("value")
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute("value")
        return value_before, value_after





class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()

        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {
            "what": {"title": self.locators.TABS_WHAT,
                     "content": self.locators.TABS_WHAT_CONTENT},
            "use": {"title": self.locators.TABS_USE,
                    "content": self.locators.TABS_USE_CONTENT},
            "origin": {"title": self.locators.TABS_ORIGIN,
                       "content": self.locators.TABS_ORIGIN_CONTENT},
            "more": {"title": self.locators.TABS_MORE,
                     "content": self.locators.TABS_MORE_CONTENT}
        }
        button = self.element_is_visible(tabs[name_tab]["title"])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]["content"]).text
        return button.text, len(what_content)

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)

        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        time.sleep(1)
        tool_tip_text_field = self.get_text_from_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        time.sleep(1)
        tool_tip_text_contrary = self.get_text_from_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        time.sleep(1)
        tool_tip_text_section = self.get_text_from_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for i in menu_item_list:
            self.action_move_to_element(i)
            # self.element_is_visible(i)
            data.append(i.text)
        return data


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable(self.locators.GRID_ITEM)
        return order_before, order_after


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_wh(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(" ", "")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ", "")
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute("style")
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_wh(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_wh(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return min_size, max_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_wh(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(
            self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_wh(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return min_size, max_size
















































