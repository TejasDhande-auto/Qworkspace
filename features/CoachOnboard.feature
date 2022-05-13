
Feature: Coach Onboarding

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach56A",email="qtestcoach+tests1@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+tests1@outlook.com")
    And : Sync the Google Calendar with platform
    Then : Coach dashboard should be open


