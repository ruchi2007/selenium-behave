Feature: Performance Page

  Scenario: user should see performance page
    Given i am in home page
    When i click performance button
    And i click my trackers btn
    And i click employee trackers btn
    Then i should see EmployeePerformanceTrackerList page