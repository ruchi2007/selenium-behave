Feature: MyinfoPage

  Scenario: user should see myinfo page
    Given i am in home page
    When i click myinfo button
    And i enter firstname
    And i enter lastname
    Then i should see myinfo page
