import time

from selenium.common.exceptions import NoSuchElementException

from automacao2.pages.PageObject import PageObject

class FooterPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_footer_displayed(self) -> bool:
        try:
            return self.driver.find_element_by_class_name('onde') != 0

        except NoSuchElementException:
            return False

    def scroll_page_to_bottom(self):
        scroll_pause_time = 2
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    def get_address(self) -> str:
        try:
            return self.driver.find_element_by_class_name('onde').find_element_by_tag_name('p').text

        except NoSuchElementException:
            return ''
