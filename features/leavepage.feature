Feature: leavePage

  Scenario: user should see leave page
    Given i am in home page
    When i click leave button
    And i click leave apply btn
    And i click leave my leave btn
    Then i should see my leave list page