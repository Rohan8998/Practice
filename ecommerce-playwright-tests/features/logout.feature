Feature: Ecommerce Logout
  Scenario: Successful logout
    Given the user is logged in to Swag Labs
    When the user clicks logout
    Then the user should be redirected to the login page
