from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("xpath=//input[@name='username']")
        self.password_input = page.locator("xpath=//input[@name='password']")
        self.login_button = page.locator("xpath=//*[@type='submit']")
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()