from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_btn = (By.ID, 'login-button')

    def enter_username(self, username):
        self.enter_element(self.username_field, username)

    def enter_password(self, password):
        self.enter_element(self.password_field, password)

    def click_login(self):
        self.click_element(self.login_btn)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
