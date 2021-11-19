Feature: Onboard a client
  Scenario: Onboard an individual client
    Given Open the recommended browser
    When hit tempmail url
    And Copy the email address
    And Open new tab
    And  Enter the email "opsqdev2021@outlook.com" and password "Quantuvos@123"
    Then Operation user successfully login
