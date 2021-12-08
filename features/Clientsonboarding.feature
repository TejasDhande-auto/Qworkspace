Feature: Onboarding individual and customer client

  Scenario: Onboard new Individual client
    Given : Temporary mail should be opened
    When : Send an invitation to individual client
    And : Complete the onboarding process
    And : Schedule the first session
    Then : Client dashboard should be open


  Scenario: Onboard new customer client
    Given : Temporary mail should be opened
    When : Send an invitation to customer client
    And : Complete the onboarding process
    And : Schedule the first session
    Then : Client dashboard should be open