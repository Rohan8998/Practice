from playwright.sync_api import Page

class AddToCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator("xpath=//*[@id='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = page.locator("xpath=//*[@class='shopping_cart_link']")
        self.checkout_button = page.locator("xpath=//*[@id='checkout']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        self.cart_icon.click()
        self.checkout_button.click()

    def test_add_to_cart(self, page):
        self.add_to_cart()
        assert page.title() == "Swag Labs"  
        print("Add to cart successful")