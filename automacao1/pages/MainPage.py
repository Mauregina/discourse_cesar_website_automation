import time

from selenium.webdriver.common.by import By
from automacao1.pages.PageObject import PageObject
from collections import Counter

class MainPage(PageObject):
    URL_MAIN = 'https://www.discourse.org/'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_main_page_url()

    def open_main_page_url(self):
        self.driver.get(self.URL_MAIN)

    # def is_url_main_page(self):
    #     return self.driver.current_url == self.URL_MAIN

    def click_demo_item(self):
        self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/ul/li[4]/a').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])























