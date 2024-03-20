from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavbarPage(BasePage):
    def __init__(self):
        self.cart_locator = (By.CLASS_NAME, 'shopping_cart_link')
        self.menu_locator = (By.ID, 'react-burger-menu-btn')
        self.logout_btn_locator = (By.ID, 'logout_sidebar_link')

    def get_cart_count(self):
        self.get_text(self.cart_locator)

    def click_cart(self):
        self.click_element(self.cart_locator)

    def click_menu(self):
        self.click_element(self.menu_locator)

    def click_logout(self):
        self.click_menu()
        self.click_element(self.logout_btn_locator)
