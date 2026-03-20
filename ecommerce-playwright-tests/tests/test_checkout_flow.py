from playwright.sync_api import sync_playwright


def __init__(self, page: Page):
    self.page = page
    self.username_input = page.locator("xpath=//*[@id='user-name']")
    self.password_input = page.locator("xpath=//*[@id='password']")
    self.login_button = page.locator("xpath=//*[@id='login-button']")
    self.add_to_cart_button = page.locator("xpath=//*[@id='add-to-cart-sauce-labs-backpack']")
    self.cart_icon = page.locator("xpath=//*[@class='shopping_cart_link']")
    self.checkout_button = page.locator("xpath=//*[@id='checkout']")
    self.first_name_input = page.locator("xpath=//*[@id='first-name']")
    self.last_name_input = page.locator("xpath=//*[@id='last-name']")
    self.zip_code_input = page.locator("xpath=//*[@id='postal-code']")
    self.continue_button = page.locator("xpath=//*[@id='continue']")
    self.finish_button = page.locator("xpath=//*[@id='finish']")

def test_checkout_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        self.username_input.fill("standard_user")
        self.password_input.fill("secret_sauce")
        self.login_button.click()
        page.wait_for_url("https://www.saucedemo.com/inventory.html")
        assert page.title() == "Swag Labs"  
        print("Login successful")
        page.wait_for_timeout(5000)

        self.add_to_cart_button.click()
        self.cart_icon.click()
        self.checkout_button.click()
        page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
        assert page.title() == "Swag Labs"  
        print("Add to cart successful")
        page.wait_for_timeout(5000)

        self.first_name_input.fill("John")
        self.last_name_input.fill("Doe")
        self.zip_code_input.fill("12345")
        self.continue_button.click()
        page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
        assert page.title() == "Swag Labs"  
        print("Fill your information successful")
        page.wait_for_timeout(5000)

        self.finish_button.click()
        page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
        assert page.title() == "Swag Labs"  
        print("Finish successful")
        page.wait_for_timeout(5000)
    
        
        browser.close()

if __name__ == "__main__":
    test_checkout_flow()