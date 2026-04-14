import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.add_to_cart import AddToCartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

def test_checkout_flow(page):
    # Log in
    log_in_page = LogInPage(page)
    log_in_page.login("standard_user", "secret_sauce")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    assert page.title() == "Swag Labs"
    print("Login successful")
    
    # Add to cart
    add_to_cart_page = AddToCartPage(page)
    add_to_cart_page.add_to_cart()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    assert page.title() == "Swag Labs"
    print("Add to cart successful")

    # Your Information
    your_information_page = YourInformationPage(page)
    your_information_page.fill_your_information()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    assert page.title() == "Swag Labs"
    print("Fill your information successful")

    # Finish
    overview_page = OverviewPage(page)
    overview_page.finish()
    page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
    assert page.title() == "Swag Labs"
    print("Finish successful")