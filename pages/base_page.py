from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from shared.common_base import CommonBase


class BasePage(CommonBase):
    def enter_element(self, locator, text):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        element.send_keys(text)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        element.click()
