Feature: Set user password
Scenario Outline: Set Password
Given Open Browser
When Navigate to the page
And Enter password "<password>" and confirm password "<Confirm password>"
Then password save successfully

Examples:
    |  password  |  Confirm password  |
    |  admin  |  admin123  |
    | Qwerty123  |  Qwerty123  |
    | Qwerty@123  |  Qwerty@123  |
    | Abc@12345  |  Abc@12345  |