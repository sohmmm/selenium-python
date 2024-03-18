from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from shared.common_base import CommonBase


class LoginPage(CommonBase):
    def __init__(self):
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_btn = (By.ID, 'login-button')

    def enter_username(self, username):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.username_field))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.password_field))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.login_btn))
        element.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
