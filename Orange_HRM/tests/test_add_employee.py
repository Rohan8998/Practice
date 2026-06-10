from playwright.sync_api import Page
from Orange_HRM.pages.login_page import LoginPage
from Orange_HRM.pages.dashboard_page import DashboardPage
import json
import os

# Load credentials
credentials_path = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')
with open(credentials_path, 'r') as f:
    credentials = json.load(f)

# Load employee details
employee_details_path = os.path.join(os.path.dirname(__file__), '..', 'employee_details.json')
with open(employee_details_path, 'r') as f:
    employee_details = json.load(f)


def test_add_employee(page):
    # Login
    login_page = LoginPage(page)
    login_page.login(credentials['username'], credentials['password'])
    page.wait_for_url("**/dashboard/index")
    assert page.title() == "OrangeHRM"
    print("Login successful")

    # Navigate to PIM > Add Employee
    dashboard_page = DashboardPage(page)
    dashboard_page.click_pim()
    page.wait_for_url("**/pim/viewEmployeeList")
    dashboard_page.click_add_employee_tab()
    page.wait_for_url("**/pim/addEmployee")

    # Upload profile picture
    dashboard_page.upload_profile_picture(employee_details.get('photo'))

    # Fill employee details from JSON
    dashboard_page.fill_employee_details(
        first_name=employee_details['firstname'],
        middle_name=employee_details['middlename'],
        last_name=employee_details['lastname'],
        employee_id=employee_details.get('Employee_id')
    )

    # Click Save
    dashboard_page.click_save()
    print("Employee added successfully")
