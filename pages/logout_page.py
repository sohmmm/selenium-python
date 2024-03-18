from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from shared.common_base import CommonBase


class LogoutPage(CommonBase):
    def __init__(self):
        self.menu_btn = (By.ID, 'react-burger-menu-btn')
        self.logout_link = (By.ID, 'logout_sidebar_link')

    def click_menu_btn(self):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.menu_btn))
        element.click()

    def click_logout(self):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.logout_link))
        element.click()

    def logout(self):
        self.click_menu_btn()
        self.click_logout()
