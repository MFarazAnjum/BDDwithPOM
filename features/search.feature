Feature: Search functionality
  Background: Navigate to Home Page
    Given I Navigate to Home Page

  Scenario: Search for a valid product
    When I enter valid product name in search field
    And I click on search button
    Then Valid product displayed in search results


  Scenario: Search for a invalid product
    When I enter invalid product name in search field
    And I click on search button
    Then Proper message should be displayed in search results

  Scenario: Search without entering any product
    When I dont enter anything in search field
    And I click on search button
    Then Proper message should be displayed in search results

