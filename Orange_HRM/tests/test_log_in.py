from playwright.sync_api import Page
from Orange_HRM.pages.login_page import LoginPage
import json

import os

credentials_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')
with open(credentials_path, 'r') as f:
    credentials = json.load(f)

def test_login(page):
    login_page = LoginPage(page)
    login_page.login(credentials['username'], credentials['password'])
    page.wait_for_url("**/dashboard/index")
    assert page.title() == "OrangeHRM"
    print("Login successful")