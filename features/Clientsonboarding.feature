Feature: Onboarding individual and customer client

  Scenario: Onboard new Individual client
    When : Send an invitation to individual client (name="IndAutoClient02July",email="qtestclient+self02July@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+self02July@outlook.com")
    And : Sync the Google Calendar
    And : Schedule the first session (email="qtestclient+self02July@outlook.com")
    Then : Client dashboard should be open


  Scenario: Onboard new customer client
    When : Send an invitation to customer client (name="CustAutoClient02July",email="qtestclient+cust02July@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+cust02July@outlook.com")
    And : Sync the MS calendar
    And : Schedule the first session (email="qtestclient+cust02July@outlook.com")
    Then : Client dashboard should be open