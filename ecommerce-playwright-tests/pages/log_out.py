from playwright.sync_api import Page

class LogOutPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.locator("xpath=//*[@id='react-burger-menu-btn']")
        self.logout_button = page.locator("xpath=//*[@id='logout_sidebar_link']")

    def log_out(self):
        self.menu_button.click()
        self.logout_button.click()

    def test_log_out(self, page):
        self.log_out()
        assert page.title() == "Swag Labs"  
        print("Log out successful")