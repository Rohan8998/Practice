import sys
import os
import json
# Add the project directory to sys.path so python can find "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.log_in_page import LogInPage
from pages.add_to_cart import AddToCartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from pages.log_out import LogOutPage

data_path = os.path.join(os.path.dirname(__file__), '..', 'test_data.json')
with open(data_path, "r") as f:
    test_data = json.load(f)
    username = test_data["username"]
    password = test_data["password"]

def test_log_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        log_in_page = LogInPage(page)
        log_in_page.test_error_message(page)
        log_in_page.login(username, password)
        page.wait_for_url("https://www.saucedemo.com/inventory.html")
        assert page.title() == "Swag Labs"  
        print("Login successful")
        page.wait_for_timeout(5000)

        

if __name__ == "__main__":
    test_log_in()
