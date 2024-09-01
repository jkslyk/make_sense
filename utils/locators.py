from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGO = (By.XPATH, '/html/head/meta[9]')
    SEARCH_ICON = (By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[2]/div/div[2]/div[1]/a/div/div/img')

class SearchPageLocators(object):
    SEARCH_BOX = (By.XPATH, '//*[@id="__next"]/main/div/div[3]/div/div/div/div[1]/div/div/form/input')  # Replace with the actual path to the search input field
    SEARCH_RESULTS = (By.XPATH, '//*[@id="__next"]/main/div/div[3]/div/div/div/div[2]/div/div')  # Replace with the actual path to the search results