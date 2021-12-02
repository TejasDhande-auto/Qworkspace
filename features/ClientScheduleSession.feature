Feature: Schedule a session by client
  Scenario: Session scheduling
    Given Client should logged in
    When Schedule first session of client
    Then First session should be scheduled
