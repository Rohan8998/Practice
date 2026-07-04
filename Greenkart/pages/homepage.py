from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search = page.locator("input.search-keyword")
        self.cart = page.locator("a.cart-icon")

    def search_product(self, product):
        self.search.fill(product)
        self.searched_product = product
    
    def fill_qty(self, quantity):
        product_card = self.page.locator(".product", has_text=self.searched_product)
        product_card.locator("input.quantity").fill(quantity)

    def click_add_to_cart(self):
        product_card = self.page.locator(".product", has_text=self.searched_product)
        product_card.locator("button:has-text('ADD TO CART')").click()

    def click_cart(self):
        self.cart.click()