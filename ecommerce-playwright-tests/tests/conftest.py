import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import json
import os

@pytest.fixture(scope="session")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.json')
    with open(data_path) as f:
        return json.load(f)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)
