import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.add_to_cart import AddToCartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from pages.log_out import LogOutPage

with open("test_data.json", "r") as f:
    test_data = json.load(f)
    username = test_data["username"]
    password = test_data["password"]

def test_log_in(page):
    log_in_page = LogInPage(page)
    
    # Optional logic inside POM that we run first
    log_in_page.test_error_message(page)
    
    # Reload because test_error_message does a failed login
    page.goto("https://www.saucedemo.com")
    
    log_in_page.login(username, password)
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    assert page.title() == "Swag Labs"  
    print("Login successful")
