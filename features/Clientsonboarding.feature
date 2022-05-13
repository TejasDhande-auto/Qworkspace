Feature: Onboarding individual and customer client

  Scenario: Onboard new Individual client
    When : Send an invitation to individual client (name="IndAutoClient1c",email="qtestclient+self1c@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+self1c@outlook.com")
    And : Sync the Google Calendar
    And : Schedule the first session (email="qtestclient+self1c@outlook.com")
    Then : Client dashboard should be open


  Scenario: Onboard new customer client
    When : Send an invitation to customer client (name="CustAutoClient1c",email="qtestclient+cust1c@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+cust1c@outlook.com")
    And : Sync the MS calendar
    And : Schedule the first session (email="qtestclient+cust1c@outlook.com")
    Then : Client dashboard should be open