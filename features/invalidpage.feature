Feature: loginPage
  Scenario: user should not login with invalid credential
    Given i go to login page
    When i enter invalid username
    And i enter invalid password
    And i click submit btn
    Then i should see error message