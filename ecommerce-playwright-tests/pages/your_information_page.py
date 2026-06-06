from playwright.sync_api import Page

class YourInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("xpath=//*[@id='first-name']")
        self.last_name_input = page.locator("xpath=//*[@id='last-name']")
        self.zip_code_input = page.locator("xpath=//*[@id='postal-code']")
        self.continue_button = page.locator("xpath=//*[@id='continue']")

    def fill_your_information(self):
        self.first_name_input.fill("John")
        self.last_name_input.fill("Doe")
        self.zip_code_input.fill("12345")
        self.continue_button.click()