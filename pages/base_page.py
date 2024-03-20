from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from shared.common_base import CommonBase


class BasePage(CommonBase):
    def get_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located(locator))
        return elements

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def enter_element(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def get_element_by_name(self, locator, name):
        elements = self.get_elements(locator)

        for element in elements:
            if element.find_element(By.CLASS_NAME, 'inventory_item_name').text == name:
                return element

        return None

