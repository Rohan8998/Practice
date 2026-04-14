import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.log_out import LogOutPage

def test_log_out(page):
    # Log in
    log_in_page = LogInPage(page)
    log_in_page.login("standard_user", "secret_sauce")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    assert page.title() == "Swag Labs"
    print("Login successful")

    # Log out
    log_out_page = LogOutPage(page)
    log_out_page.log_out()
    page.wait_for_url("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"
    print("Log out successful")