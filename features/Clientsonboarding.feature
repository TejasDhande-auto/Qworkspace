Feature: Onboarding individual and customer client

  Scenario: Onboard new Individual client
    When : Send an invitation to individual client (name="IndAutoClient2",email="qtestclient+self4@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+self4@outlook.com")
    And : Schedule the first session (email="qtestclient+self4@outlook.com")
    Then : Client dashboard should be open


  Scenario: Onboard new customer client
    When : Send an invitation to customer client (name="CustAutoClient2",email="qtestclient+cust4@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+cust4@outlook.com")
    And : Schedule the first session (email="qtestclient+cust4@outlook.com")
    Then : Client dashboard should be open