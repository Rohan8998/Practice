import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    
    browser_str = str(browser_name).lower()
    
    with sync_playwright() as p:
        if "firefox" in browser_str:
            browser = p.firefox.launch(headless=False, slow_mo=1000)
        else:
            browser = p.chromium.launch(headless=False, slow_mo=1000)

        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    yield page
    page.close()