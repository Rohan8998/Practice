from playwright.sync_api import Page

class LogInPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("xpath=//*[@id='user-name']")
        self.password_input = page.locator("xpath=//*[@id='password']")
        self.login_button = page.locator("xpath=//*[@id='login-button']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    
    def test_invalid_login(self, page):
        self.login("invalid_user", "wrong_password")

        assert "inventory" not in page.url

    def test_empty_password(self, page):
        self.login("standard_user", "")

        assert "inventory" not in page.url  

    def test_error_message(self, page):
        self.login("invalid_user", "wrong_password")

        assert "Epic sadface: Username and password do not match any user in this service" in page.content()    

    def test_error_message_empty_password(self, page):
        self.login("standard_user", "")

        assert "Epic sadface: Username and password do not match any user in this service" in page.content()    