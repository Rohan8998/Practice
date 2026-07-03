Feature: OrangeHRM Add Employee
  Scenario: Successful addition of a new employee
    Given the user is logged in
    When the user navigates to Add Employee page
    And the user enters employee details and uploads profile picture
    And the user clicks save
    Then the employee should be successfully added
