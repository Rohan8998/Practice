import sys
import os
import json
import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.log_in_page import LogInPage
from pages.add_to_cart import AddToCartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage
from pages.log_out import LogOutPage

# Load scenarios from features directory
scenarios('../features')

# Load test data
with open(os.path.join(os.path.dirname(__file__), '..', 'test_data.json'), "r") as f:
    test_data = json.load(f)
    username = test_data["username"]
    password = test_data["password"]


# --- Web UI Step Definitions ---

@given("the user is on the Swag Labs login page")
def on_swag_labs_login(page):
    if page.url == "about:blank":
        page.goto("https://www.saucedemo.com")


@when("the user logs in with username and password")
def user_login(page):
    log_in_page = LogInPage(page)
    # Optional logic inside POM that we run first (like verify error message on failed log in)
    log_in_page.test_error_message(page)
    
    # Reload because test_error_message does a failed login
    page.goto("https://www.saucedemo.com")
    log_in_page.login(username, password)


@then("the user should see the products inventory page")
def check_inventory_page(page):
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    assert page.title() == "Swag Labs"
    print("Login successful")


@given("the user is logged in to Swag Labs")
def user_logged_in_to_swag_labs(page):
    log_in_page = LogInPage(page)
    log_in_page.login("standard_user", "secret_sauce")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    assert page.title() == "Swag Labs"
    print("Login successful")


@when("the user clicks logout")
def user_logout(page):
    log_out_page = LogOutPage(page)
    log_out_page.log_out()


@then("the user should be redirected to the login page")
def check_login_page_redirect(page):
    page.wait_for_url("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"
    print("Log out successful")


@when("the user adds an item to the cart")
def user_adds_item_to_cart(page):
    add_to_cart_page = AddToCartPage(page)
    add_to_cart_page.add_to_cart()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    assert page.title() == "Swag Labs"
    print("Add to cart successful")


@when("the user fills checkout information")
def user_fills_checkout_info(page):
    your_information_page = YourInformationPage(page)
    your_information_page.fill_your_information()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    assert page.title() == "Swag Labs"
    print("Fill your information successful")


@when("the user completes the purchase")
def user_completes_purchase(page):
    overview_page = OverviewPage(page)
    overview_page.finish()


@then("the order should be completed successfully")
def check_order_complete(page):
    page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
    assert page.title() == "Swag Labs"
    print("Finish successful")


# --- API Step Definitions ---

@pytest.fixture
def api_context():
    return {}


@when(parsers.parse("the user requests user details for ID {user_id:d}"))
def get_user_details(user_id, api_context):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    api_context["response"] = response
    with open('user_data.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
        print("Data saved to user_data.json")


@then(parsers.parse("the response status code should be {status_code:d}"))
def check_api_status_code(status_code, api_context):
    assert api_context["response"].status_code == status_code


@then(parsers.parse('the user\'s name should be "{expected_name}"'))
def check_api_user_name(expected_name, api_context):
    data = api_context["response"].json()
    assert data['name'] == expected_name
    assert data['email'] == 'Sincere@april.biz'
    assert data['address']['city'] == 'Gwenborough'


@when("the user submits a POST request to create a user")
def create_user_api(api_context):
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name": "Rohan Tester",
        "username": "rohan_t",
        "email": "rohan.testing@example.com",
        "address": {
            "street": "Balaji Nagar",
            "suite": "Aarti Apt",
            "city": "Pune",
            "zipcode": "411043",
            "geo": {
                "lat": "18.5204",
                "lng": "73.8567"
            }
        },
        "Hometown":"Pune"
    }
    response = requests.post(url, json=payload)
    api_context["response"] = response


@then("the response should contain a new user ID")
def check_created_user_id(api_context):
    data = api_context["response"].json()
    assert "id" in data
    assert data["name"] == "Rohan Tester"
    assert data["address"]["city"] == "Pune"
    assert data["address"]["zipcode"] == "411043"
    assert data["Hometown"] == "Pune"
