Feature: Register account Functionality
  Background: Navigation
    Given I navigate to Register Page

  Scenario: Register with mandatory fields
    When I enter mandatory Fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with all fields
    When I enter all Fields
    And I click on continue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    When I enter all Fields except email field
    And I enter existing accounts email into email field
    And I click on continue button
    Then Proper warning message should be displayed for duplicate emails

  Scenario: Register without providing any details
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning message should be displayed for mandatory field should be entered