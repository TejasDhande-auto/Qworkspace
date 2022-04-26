
Feature: Coach Onboarding

  Scenario: Onboard new coach
    When : Send an invitation to coach (name="QTestCoach3A",email="qtestcoach+test3@outlook.com")
    And : Complete the coach onboarding process (email="qtestcoach+test3@outlook.com")
    And : Sync the Google Calendar
    Then : Coach dashboard should be open


