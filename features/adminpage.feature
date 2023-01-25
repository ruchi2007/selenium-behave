Feature: adminPage

  Background: common steps
    Given i am in home page
    When i click admin button

  Scenario: user should see admin page
    When i click System_Users_user_role_icon
    And i click System_Users_status_icon
    And I click add btn
    Then i should see add user page

  Scenario: user should see job titles page
    When i click jobs btn
    And I click job titles btn
    Then i should see job titles page

  Scenario: user should see organization page
    When i click organization btn
    And i click organization_locations btn
    Then i should see organization_locations page

  Scenario: user should see qualifications page
    When i click qualifications btn
    And i click qualifications_education btn
    Then i should see qualifications_education page

  Scenario: user should see nationalities page
    When i click nationalities
    Then i should see nationalities page


