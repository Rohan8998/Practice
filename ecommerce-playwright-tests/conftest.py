import pytest
import os
import pytest_html
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports", exist_ok=True)
            screenshot_path = os.path.join("reports", f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            extras.append(pytest_html.extras.png(screenshot_path))
            report.extras = extras