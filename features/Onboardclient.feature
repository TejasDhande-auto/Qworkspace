Feature: Onboard Client
  Scenario: Onboard Individual Client
    Given Hit the Chrome browser
    When  Hit the tempory mail URL
    And Copy the mail
    And Open the new tab
    And Hit the quantuvos URL
    And Enter "opsqdev2021@outlook.com" and "Quantuvos@123" and click on submit
    And Onboard New client
