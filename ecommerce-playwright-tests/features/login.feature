Feature: Ecommerce Login
  Scenario: Successful login with valid credentials
    Given the user is on the Swag Labs login page
    When the user logs in with username and password
    Then the user should see the products inventory page
