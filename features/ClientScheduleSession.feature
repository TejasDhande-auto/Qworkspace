Feature: Schedule a session by client
  Scenario: Session scheduling
    Given Open browser and hit the login URL
    When Enter client email "qclientprofile@gmail.com" and password "1234Test.".
    And Go to the session screen
    And right click on one of the date
    And click on Schedule Session
    And Select Date and time and click on save
    Then Sesion has been scheduled
