Feature: Onboard individual client
  Scenario: Onboard individual client
    Given Hit Chrome browser
    When Hit the temp mail link
    And Copy the temp email address
    And Open new tab
    And Hit the Qunatuvos login URL and logged in as operation user "opsqdev2021@outlook.com" and "Quantuvos@123"
    And Send invitation to individual client
    And Go to the temp mail
    And Open the first Email and click on Start
    And Paste the temp email address and click on Send
    And Again hit the temp mail link
    And Open confirm password email and click on Confirm
    And Enter the password "Qwerty@123" and "Qwerty@123" and click on next
    And Again hit the Quantuvos login URL
    And paste the email address and enter password "Qwerty@123" and click on login
    And client form opened and filled the details
    And Operation user selects three coaches
    And Again client logged in
    And select one of the coach
    And Schedule first session
    Then Popup should display

