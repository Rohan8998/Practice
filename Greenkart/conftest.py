from playwright.sync_api import Playwright, sync_playwright
import pytest


@pytest.fixture(scope="session")
def headless():
    return False

@pytest.fixture()
def launch(page, headless):  
    # it is not working as headless is not getting passed                   
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.wait_for_load_state('networkidle')

    yield page
    page.close()
