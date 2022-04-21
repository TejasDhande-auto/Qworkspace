
Feature: Coach Onbaording

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach1",email="qtestcoach+1@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+1@outlook.com")
    Then : Coach dashboard should be open


