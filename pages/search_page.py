from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = SearchPageLocators

    def search(self, text):
        main_page = MainPage(self.driver)
        main_page.open_search_page()

        # Step 2: Wait for the search box to be present and then interact with it
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.SEARCH_BOX)  # Передайте локатор как кортеж
        )
        search_box.clear()
        search_box.send_keys(text)
        search_box.submit()

        return search_box.get_attribute("value")

    def search_results(self):
        # Wait for search results to load
        results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locator.SEARCH_RESULTS)  # Передайте локатор как кортеж
        )
        return results
