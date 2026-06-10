from playwright.sync_api import sync_playwright
import pytest



@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page_obj = context.new_page()
        page_obj.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield page_obj
        context.close()
        browser.close()