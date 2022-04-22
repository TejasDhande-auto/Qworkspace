Feature: Onboarding individual and customer client

  Scenario: Onboard new Individual client
    When : Send an invitation to individual client (name="IndAutoClient6",email="qtestclient+self6@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+self6@outlook.com")
    And : Schedule the first session (email="qtestclient+self6@outlook.com")
    Then : Client dashboard should be open


  Scenario: Onboard new customer client
    When : Send an invitation to customer client (name="CustAutoClient6",email="qtestclient+cust6@outlook.com",hours="10")
    And : Complete the onboarding process (email="qtestclient+cust6@outlook.com")
    And : Schedule the first session (email="qtestclient+cust6@outlook.com")
    Then : Client dashboard should be open