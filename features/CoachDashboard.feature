Feature: Verify  Coach Dashboard

  Scenario: Verify Coach login successfully
    When Login page should be open
    And Enter coach credentials "qtestcoach+calendarsync@gmail.com" and "Qwerty@123"
    Then Coach dashboard should display

  Scenario: Verify Missing survey section on Calendar screen
    When Verify missing survey are pending
    And If pending click one of missing survey
    And Submit the survey
    Then Survey should be submitted

  Scenario: Verify Calendar on Calendar screen
    When Click on Week
    Then Week view should display on screen
    And Click on Month
    Then Month view should display on screen

  Scenario: Verify Client to be reschedule section on Calendar screen
    When Verify the client list
    And Click one of client
    Then Selected client details screen should be open

  Scenario: Verify filter functionality on client column on Clients screen
    When Click on filter and enter "Qtest" as client name
    Then Client details screen should open

  Scenario: Verify Session scheduling functionality
    When Click on Schedule+ button
    Then Schedule next session calendar should display
    When Select and date and time and click on save
    Then Session should be scheduled

  Scenario: Verify notes section under client details screen
    When Crete or edit note for client
    Then Created/edited note should display on screen

  Scenario: Verify Activities section under client details screen
    When Check activities are assigned to client
    And  click one of activity if assigned
    Then Activity should open

  Scenario: Verify Add activity to client functionality
    When Click on Add button and select resource from NetQ
    Then Proper toaster message should display to coach

   Scenario: Verify Client profile section under client details screen
     When Check client profile is loading
     Then Client profile should load successfully

   Scenario: Verify Sessions section under client details screen
     When Check sessions list
     Then Session list should display

   Scenario: Verify Chat section under client details screen
     When Send message to client
     Then Message should sent

   Scenario: Verify Coach-Network Q Resources screen on is displayed
    When  Click on Coach-Network Q Resources
    Then  Coach-Network Q Resources screen should be open

  Scenario: Verify Tab switching on Coach-Network Q Resources screen
    When Click on Tabs on Coach-Network Q Resources
    Then Tab related resources should display to coach on screen

  Scenario: Verify Search functionality on Coach-Network Q Resources screen
    When Enter text in search box on Coach-Network Q Resources screen
    Then Matched resources should display to coach

  Scenario: Verify Advanced search functionality on Coach-Network Q Resources screen
    When Enter text in advanced search box on Coach-Network Q Resources screen
    Then Matched resources to advanced search should display

  Scenario: Verify Submit Resource functionality on Coach-Network Q Resources screen
    Given Submit Resource modal window should be open
    When Enter the resource details and click on save
    Then Resource should be submitted for approval

  Scenario: Verify Coach profile details are displayed properly
    Given Coach-Profile & Preferences screen should display
    When If coach personal information display
    Then Coach Profile details displayed properly

  Scenario: Verify Coach profile details are updated properly
    When Enter text in field and click on submit
    Then Coach profile should be updated and updated value should display in field

  Scenario: Verify Coach-Settings screen is displayed
    When Click on Coach-Settings
    Then Coach-Settings screen should displayed

  Scenario: Verify Add/Change MS calendar functionality for coach
    When Add/Change outlook calendar for coach
    Then Outlook calendar details should display on coach's settings screen

  Scenario: Verify delete calendar functionality for coach
    When Click on delete calendar
    Then Coach-Calendar should be deleted from platform

  Scenario: Verify Add/Change Google calendar functionality for coach
    When Add Google calendar for coach
    Then Google calendar details should display on coach's settings screen

  Scenario: Verify Change password functionality for coach
    When Click on change password icon
    And Enter Incorrect old password and New password and click on Submit
    Then Appropriate error message should display on screen

  Scenario: Verify Logout functionality for coach dashboard
    When Click on Logout
    Then Login page should display

