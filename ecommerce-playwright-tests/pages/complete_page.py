from playwright.sync_api import Page

class CompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.back_to_products_button = page.locator("xpath=//*[@id='back-to-products']")

    def back_to_products(self):
        self.back_to_products_button.click()

    def test_back_to_products(self, page):
        self.back_to_products()
        assert page.title() == "Swag Labs"  
        print("Back to products successful")