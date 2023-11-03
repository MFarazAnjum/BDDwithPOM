Feature: Login Functionality

  Background:
    Given I navigate to Login Page


  Scenario: Login with Valid Credentials
    When I enter valid email and password
    And I click on login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    When I enter valid email and invalid password
    And I click on login button
    Then I should get proper warning


  Scenario: Login with valid email and invalid password
    When I enter valid email and invalid password
    And I click on login button
    Then I should get proper warning

  Scenario: Login with invalid Credentials
    When I enter invalid email and password
    And I click on login button
    Then I should get proper warning

  Scenario: Login without entering any Credentials
    When I enter invalid email and password
    And I click on login button
    Then I should get proper warning


