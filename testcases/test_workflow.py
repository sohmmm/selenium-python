import pytest

from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetailsPage
from shared.common_base import CommonBase
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.utils import read_excel


class TestWorkflow(CommonBase):
    common_base = CommonBase()
    inventory_page = InventoryPage()
    product_details_page = ProductDetailsPage()

    @pytest.fixture(autouse=True, scope='session')
    def before_launch(self):
        self.common_base.initialize()
        self.common_base.launch_browser('https://www.saucedemo.com')
        yield
        self.common_base.quit_driver()

    def test_login(self):
        login_page = LoginPage()
        username, password = 'standard_user', 'secret_sauce'  # username, password
        login_page.login(username, password)

        obtained_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory.html'

        assert obtained_url == expected_url

    def test_product_link(self):
        product_name = 'Sauce Labs Bike Light'
        self.inventory_page.click_product(product_name)

        obtained_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory-item.html'

        assert expected_url in obtained_url

    def test_product_is_same_as_clicked(self):
        expected_name = 'Sauce Labs Bike Light'
        expected_price = '$9.99'

        obtained_name = self.product_details_page.get_name()
        obtained_price = self.product_details_page.get_price()

        assert obtained_name == expected_name
        assert obtained_price == expected_price

    # def test(self):
    #     self.product_details_page.click_add_to_cart()
    #     self.product_details_page.click_back_btn()
    #
    #     self.inventory_page.click_add_to_cart('Sauce Labs Bike Light')


