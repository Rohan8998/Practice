from playwright.sync_api import Page
from Greenkart.pages.homepage import HomePage
import json
import os

# Load test data
with open(os.path.join(os.path.dirname(__file__), '..', 'product.json'), 'r') as file:
    product_data = json.load(file)

def test_add_to_cart(launch):
    home_page = HomePage(launch)
    home_page.search_product(product_data['product'])
    home_page.fill_qty(product_data['quantity'])
    home_page.click_add_to_cart()
