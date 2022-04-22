
Feature: Coach Onboarding

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach3A",email="qtestcoach+3@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+3@outlook.com")
    Then : Coach dashboard should be open


