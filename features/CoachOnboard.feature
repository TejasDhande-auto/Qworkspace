Feature: Onboard of a new coach
  Scenario: Coach Onboarding
    Given Laumch the browser
    And open the Hit the temp URL
    And Copy the temp email address
    And Login as operation user
    And Send Invitation to coach
    And Again go to temp
    And select mail and Click on Start
    And Confirm the email address
    And Once again go to temp
    And Select mail and click on confirm
    And Set the password
    And login as coach user
    And Fill the coach detail
    Then Coach profile submitted


