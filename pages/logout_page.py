from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self):
        self.menu_btn = (By.ID, 'react-burger-menu-btn')
        self.logout_link = (By.ID, 'logout_sidebar_link')

    def click_menu_btn(self):
        self.click_element(self.menu_btn)

    def click_logout(self):
        self.click_element(self.logout_link)

    def logout(self):
        self.click_menu_btn()
        self.click_logout()
