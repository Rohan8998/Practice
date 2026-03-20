from playwright.sync_api import sync_playwright


def __init__(self, page: Page):
    self.page = page
    self.username_input = page.locator("xpath=//*[@id='user-name']")
    self.password_input = page.locator("xpath=//*[@id='password']")
    self.login_button = page.locator("xpath=//*[@id='login-button']")
    self.menu_button = page.locator("xpath=//*[@id='react-burger-menu-btn']")
    self.logout_button = page.locator("xpath=//*[@id='logout_sidebar_link']")

def test_log_out():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        browser.close()

        self.username_input.fill("standard_user")
        self.password_input.fill("secret_sauce")
        self.login_button.click()
        page.wait_for_url("https://www.saucedemo.com/inventory.html")
        assert page.title() == "Swag Labs"  
        print("Login successful")
        page.wait_for_timeout(5000)

        self.menu_button.click()
        self.logout_button.click()
        page.wait_for_url("https://www.saucedemo.com")
        assert page.title() == "Swag Labs"  
        print("Log out successful")
        page.wait_for_timeout(5000)

if __name__ == "__main__":
    test_log_out()