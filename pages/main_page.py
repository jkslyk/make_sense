
from pages.base_page import BasePage
from utils.locators import *


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super(MainPage, self).__init__(driver)

    def open_search_page(self):
        self.find_element(*self.locator.SEARCH_ICON).click()