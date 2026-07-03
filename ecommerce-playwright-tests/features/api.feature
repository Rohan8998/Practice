Feature: Fake User API
  Scenario: Get a single user details
    When the user requests user details for ID 1
    Then the response status code should be 200
    And the user's name should be "Leanne Graham"

  Scenario: Create a new user
    When the user submits a POST request to create a user
    Then the response status code should be 201
    And the response should contain a new user ID
