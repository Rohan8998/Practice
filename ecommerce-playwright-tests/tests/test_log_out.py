import sys
import os
import json

# Add the project directory to sys.path so python can find "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.log_out import LogOutPage

data_path = os.path.join(os.path.dirname(__file__), '..', 'test_data.json')
with open(data_path, "r") as f:
    test_data = json.load(f)
    username = test_data["username"]
    password = test_data["password"]

def test_log_out(page):
    page.goto("https://www.saucedemo.com")
    
    # Log in first
    log_in_page = LogInPage(page)
    log_in_page.login(username, password)
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    
    # Log out
    log_out_page = LogOutPage(page)
    log_out_page.log_out()
    
    # Assert successful logout by checking the URL returns to the login page
    page.wait_for_url("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"  
    print("Log out successful")
