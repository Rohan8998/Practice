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

    def test_fill_your_information(self, page):
        self.fill_your_information()
        assert page.title() == "Swag Labs"  
        print("Fill your information successful")

    def test_click_continue_button(self, page):
        self.continue_button.click()
        assert page.title() == "Swag Labs"  
        print("Click continue button successful")