import pytest
from shared.common_base import CommonBase
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.utils import read_excel


class TestLogin:
    @pytest.fixture(autouse=True, scope='session')
    def before_launch(self):
        cb = CommonBase()
        cb.initialize()
        cb.launch_browser('https://www.saucedemo.com')
        yield
        cb.quit_driver()

    @staticmethod
    def get_login_data():
        # ToDo make it relative
        data = read_excel('C:/Users/soham_pagi/PycharmProjects/automation-testing/test_data/login_credentials.xlsx',
                          'Login Credentials')

        for index, row in data.iterrows():
            yield row['username'], row['password']

    @pytest.mark.parametrize('login_data', get_login_data())
    def test_login(self, login_data):
        login_page = LoginPage()
        logout_page = LogoutPage()

        username, password = login_data  # username, password
        login_page.login(username, password)

        obtained_url = CommonBase.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory.html'

        assert obtained_url == expected_url

        logout_page.logout()


# TestLogin.get_login_data()
