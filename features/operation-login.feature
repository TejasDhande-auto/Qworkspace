Feature: Operation Dashboard Functionality

  Background:
    Given Launch the browser
    When Open the login Url
    And Enter email "admin@quantuvos.com" and password "Qwerty123@"
    And Click on Login
    Then Login successful


  Scenario Outline: Individual-client onboarding
    When Click on Onboarding
    And Select Individual client
    And Enter "<individualfirstname>", "<individuallastname>", "<individualemail>", "<individualallocatedcoachinghours>"
    And  Submit individual client details
    Then Email invitation send to individual-client

    Examples:
      | individualfirstname | individuallastname | individualemail | individualallocatedcoachinghours |
      | Test                | usera              | abc@xyz.com     | 120                              |
      | Test                | userb              | ab@xyz.com      | 200                              |
      | Test                | userc              | a@abxyz.com     | 500                              |
      | Test                | userd              | iufywhd.gmail   | 200                              |


  Scenario Outline: Customer-Client onboarding
    When Click on Onboarding
    And Select Customer-client
    And Enter the "<customerfirstname>", "<customerlastname>", "<customeremail>", "<customercompanyid>", "<customermanagername>", "<customerhrmanagername>", "<customerallocatedcoachinghours>" details
    And Submit customer client details
    Then Email invitation send to customer-client

    Examples:
      | customerfirstname | customerlastname | customeremail | customercompanyid | customermanagername | customerhrmanagername | customerallocatedcoachinghours |
      | Test              | user             | xyz@gmail.com | 2                 | abc                 | xyz                   | 120                            |
      | Test              | user             | zy@gmail.com  | 3                 | abc                 | xyz                   | 120                            |
      | Test              | user             | tes95@ain.com | 2                 | abc                 | xyz                   | 120                            |
      | Test              | user             | iywhd.gmail   | 1                 | abc                 | xyz                   | 120                            |


  Scenario Outline: Coach onboarding
    When Click on Onboarding
    And Select Coach
    And Enter "<coachfirstname>", "<coachlastname>", "<coachemail>"
    And Submit coach details
    Then Email invitation send to coach

    Examples:
      | coachfirstname | coachlastname | coachemail     |
      | Test           | user          | xyz@abc.com    |
      | Test           | user          | xy@abc.com     |
      | Test           | user          | fof795@ain.com |
      | Test           | user          | iufywhd.gmail  |