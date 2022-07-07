
Feature: Coach Onboarding

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach02July",email="qtestcoach+02July@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+02July@outlook.com")
    And : Sync the Google Calendar with platform
    Then : Coach dashboard should be open


