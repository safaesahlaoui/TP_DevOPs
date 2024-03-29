# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class Infow:# pylint: disable=too-few-public-methods
    # driver = webdriver.Chrome()
    query = None
    def __init__(self):
        self.driver = \
            webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org')
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(
            By.XPATH, '//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        time.sleep(10)
