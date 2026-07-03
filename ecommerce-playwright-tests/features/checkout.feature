Feature: Ecommerce Checkout Flow
  Scenario: Successful purchase of an item
    Given the user is logged in to Swag Labs
    When the user adds an item to the cart
    And the user fills checkout information
    And the user completes the purchase
    Then the order should be completed successfully
