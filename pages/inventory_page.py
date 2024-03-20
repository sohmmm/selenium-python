from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from shared.common_base import CommonBase
from pages.login_page import LoginPage


class InventoryPage(BasePage):
    def __init__(self):
        self.products_lists_locator = (By.CLASS_NAME, 'inventory_item')
        self.add_to_cart_btn_locator = (By.CSS_SELECTOR, '.pricebar > button')

    def click_product(self, product_name):
        elements = self.get_element_by_name(self.products_lists_locator, product_name)
        element = elements.find_element(By.TAG_NAME, 'a')
        element.click()

    def click_add_to_cart(self, product_name):
        element = self.get_element_by_name(self.products_lists_locator, product_name)
        add_to_cart_btn = element.find_element(By.CSS_SELECTOR, '.pricebar > button')
        add_to_cart_btn.click()


if __name__ == '__main__':
    cb = CommonBase()
    cb.initialize()
    cb.launch_browser('https://www.saucedemo.com')
    LoginPage().login('standard_user', 'secret_sauce')

    InventoryPage().click_product('Sauce Labs Bike Light')

