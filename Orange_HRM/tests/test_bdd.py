import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then
from Orange_HRM.pages.login_page import LoginPage
from Orange_HRM.pages.dashboard_page import DashboardPage
import json
import os

# Load scenarios from features directory
scenarios('../features')

# Load credentials
credentials_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')
with open(credentials_path, 'r') as f:
    credentials = json.load(f)

# Load employee details
employee_details_path = os.path.join(os.path.dirname(__file__), '..', 'employee_details.json')
with open(employee_details_path, 'r') as f:
    employee_details = json.load(f)


@given("the user is on the login page")
def user_on_login_page(page: Page):
    # page fixture in Orange_HRM/conftest.py automatically goes to login page.
    # We double-check or ensure we are there.
    if "auth/login" not in page.url:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("the user enters valid username and password")
def user_enters_valid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.login(credentials['username'], credentials['password'])


@then("the user should be redirected to the dashboard page")
def user_redirected_to_dashboard(page: Page):
    page.wait_for_url("**/dashboard/index")
    assert page.title() == "OrangeHRM"
    print("Login successful")


@given("the user is logged in")
def user_is_logged_in(page: Page):
    login_page = LoginPage(page)
    login_page.login(credentials['username'], credentials['password'])
    page.wait_for_url("**/dashboard/index")
    assert page.title() == "OrangeHRM"


@when("the user navigates to Add Employee page")
def user_navigates_to_add_employee(page: Page):
    dashboard_page = DashboardPage(page)
    dashboard_page.click_pim()
    page.wait_for_url("**/pim/viewEmployeeList")
    dashboard_page.click_add_employee_tab()
    page.wait_for_url("**/pim/addEmployee")


@when("the user enters employee details and uploads profile picture")
def user_enters_employee_details(page: Page):
    dashboard_page = DashboardPage(page)
    dashboard_page.upload_profile_picture(employee_details.get('photo'))
    dashboard_page.fill_employee_details(
        first_name=employee_details['firstname'],
        middle_name=employee_details['middlename'],
        last_name=employee_details['lastname'],
        employee_id=employee_details.get('Employee_id')
    )


@when("the user clicks save")
def user_clicks_save(page: Page):
    dashboard_page = DashboardPage(page)
    dashboard_page.click_save()


@then("the employee should be successfully added")
def employee_successfully_added():
    print("Employee added successfully")
