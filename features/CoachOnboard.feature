
Feature: Coach Onboarding

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach7june",email="qtestcoach+7june@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+7june@outlook.com")
    And : Sync the Google Calendar with platform
    Then : Coach dashboard should be open


