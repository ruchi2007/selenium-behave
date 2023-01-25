Feature: loginPage
  Scenario: user should login successfully
    Given i go to login page
    When i enter username
    And i enter password
    And i click on submit button
    Then i should see home page