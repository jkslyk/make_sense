import unittest
from pages.search_page import SearchPage
from tests.base_test import BaseTest

class SearchPageTest(BaseTest):

    def test_search_functionality(self):
        search_page = SearchPage(self.driver)
        result_text = search_page.search("депозит")
        print(f"Search result text: {result_text}")  # Выводит результат для проверки
        self.assertTrue(result_text, "No search results text returned!")

if __name__ == "__main__":
    unittest.main()
