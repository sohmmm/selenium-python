from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self):
        self.name_locator = (By.CLASS_NAME, 'inventory_details_name')
        self.description_locator = (By.CLASS_NAME, 'inventory_details_desc')
        self.price_locator = (By.CLASS_NAME, 'inventory_details_price')
        self.add_to_cart_locator = (By.CSS_SELECTOR, '.inventory_details_desc_container > button')
        self.back_btn_locator = (By.ID, 'back-to-products')

    def get_name(self):
        return self.get_text(self.name_locator)

    def get_description(self):
        return self.get_text(self.description_locator)

    def get_price(self):
        return self.get_text(self.price_locator)

    def click_add_to_cart(self):
        self.click_element(self.add_to_cart_locator)

    def click_back_btn(self):
        self.click_element(self.back_btn_locator)
