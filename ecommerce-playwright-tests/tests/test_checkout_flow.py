import os
import sys
import json
import pytest
from playwright.sync_api import expect

# Add mapping to pages folder for Python execution (Not strictly needed for Pytest but good safety net)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.add_to_cart import AddToCartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

def test_complete_checkout_flow(page):
    # Load test data manually from the file for now
    data_path = os.path.join(os.path.dirname(__file__), '..', 'test_data.json')
    with open(data_path, "r") as f:
        test_data = json.load(f)

    # Initialize Page Objects using your actual classes
    login_page = LogInPage(page)
    add_to_cart_page = AddToCartPage(page)
    info_page = YourInformationPage(page)
    overview_page = OverviewPage(page)
    complete_page = CompletePage(page)

    # 1. Login
    page.goto("https://www.saucedemo.com")
    login_page.login(test_data["username"], test_data["password"])
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    
    # 2. Add an item to the cart & go to cart
    add_to_cart_page.add_to_cart()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    
    # 3. Fill out checkout form
    info_page.fill_your_information()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    
    # 4. Finish checkout
    overview_page.finish()
    page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
    
    # 5. Verify order complete
    assert complete_page.back_to_products_button.is_visible()
