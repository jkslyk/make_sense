import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://jusan.kz/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()