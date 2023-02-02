Feature: loginPage

  Scenario: user should login successfully with valid parameters
    Given i open login page
    When i put username "admin"
    And i put password "admin123"
    And i click on submit button
    Then i should login successfully to the dashboard page

  Scenario Outline: user should login with Multiple parameters
    Given i go to login page
    When i put username "<username>"
    And i put password "<password>"
    And i click on submit button
    Then i should login successfully to the dashboard page
    Examples:
      | username | password |
      | admin    | admin123 |
      | adminxyz | admin123 |
      | admin    | adminxyz |
