Feature: Schedule a session by client
  Scenario: Session scheduling
    Given Client should logged in with valid credential "wipofi2562@iistoria.com" , "Qwerty@123"
    When Schedule first session of client
    Then First session should be scheduled
