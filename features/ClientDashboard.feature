Feature: Verify Client Dashboard

  Scenario: Verify Client login successfully
    When Login page should be open
    And Enter client credentials as "qtestclient+demo1@gmail.com" and "Qwerty@123"
    Then Client dashboard should display

  Scenario: Verify Next Session is scheduled or not
    When Next session is not scheduled or next session is after 24 hours
    Then Join session button should be disable
    When Next session is scheduled
    Then Join session button should be enable

  Scenario: Verify Goals section on client dashboard
    When Click on Add and enter text and click on save
    Then Entered text in RichText box should display on screen
    When Clear the data and click on save
    Then Goals should be deleted

  Scenario: Verify Activities section on client dashboard
    When Active button default selected
    Then Active activities should display on home screen
    When Click on Archived
    Then Archived activities should display
    When Click on "see all" button
    Then Screen should navigate Activities screen

  Scenario: Verify Recommended on Network Q section on client dashboard
    When Click on resource
    Then Resource detail should display
    When Click on "see all" button under RNQ section
    Then Screen should navigate Network Q Resources screen

  Scenario: Verify chat section on client dashboard
    When Enter text and click on send
    Then Text should display in chat window
    When Attach file
    Then File should display in chat window

  Scenario: Verify Network Q Resources screen is displayed
    When  Click on Network Q Resources
    Then  Network Q Resources screen should be open

  Scenario: Verify Tab switching on Network Q Resources screen
    When Click on Tabs
    Then Clicked tab related resources should display on screen

  Scenario: Verify Search functionality on Network Q Resources screen
    When Search for "Networking" in client-network q
    Then Related resources should display

  Scenario: Verify Advanced search functionality on Network Q Resources screen
    When Enter text in advanced search box
    Then Related resources to advances search should display

  Scenario: Verify Sessions screen is displayed
    When  Click on Sessions
    Then  Sessions screen should be open

  Scenario: Verify active tab on sessions screen
    When Notes tab is active
    Then Missing survey tab should display "Your all caught up"
    When Missing survey tab is active
    Then Missing survey should display

  Scenario: Verify Notes section on sessions screen
    When Click Add notes
    Then Note should display under Notes section
    When Click on Edit icon
    Then Edit notes should display under Notes section
    When Click on Delete icon
    Then Note should get deleted

  Scenario: Verify Activities section on sessions screen
    When  Click one of  activity under activities section
    Then  Activity details should display

  Scenario: Verify Missing survey section on sessions screen
    Given  Missing survey section should be open
    When  Missing survey is pending
    And  Fill the missing survey
    Then  Missing survey should get submitted

  Scenario: Verify Session scheduling functionality
    When Right click on tomorrow's date and click Schedule a session
    Then Schedule next session calendar should display to client
    When Select coach available date and time and click on save
    Then Session should be scheduled with coach

  Scenario: Verify Activities screen is displayed
    When  Click on Activities
    Then  Activities screen should be open

  Scenario: Verify Active activities on Activities screen
    When  Click on Active
    Then  Active activities should display
    When  Click on Coach recommended active activity
    Then  Activity detail should display and Complete button should display
    When  Click on self active activity
    Then  Activity detail should display and Complete and Delete button should display
    And  Click on Add
    Then  Screen should navigate to Network Q screen
    And  Add Self activity for client
    Then  Proper toaster messgae should display

  Scenario: Verify Archived activities Activities screen
    When  Click on Archived on activities screen
    Then  Archived activities should display on activities screen
    And  Click on Coach recommended archived activity
    Then  Activity detail should display
    And  Click on Coach self archived activity
    Then  Activity detail should display on popup


  Scenario: Verify Client profile details are displayed properly
    Given Profile & Preferences screen should display
    When If personal information display
    Then Client Profile details displayed properly

  Scenario: Verify Client profile details are updated properly
    When Enter text in field and click on save
    Then Profile should be updated and updated value should display in field

  Scenario: Verify Settings screen is displayed
    When Click on Settings
    Then Settings screen should displayed

  Scenario: Verify Add/Change MS calendar functionality for client
    When Add/Change outlook calendar for client
    Then Outlook calendar details should display on Client's settings screen

  Scenario: Verify delete calendar functionality for client
    When Click on delete
    Then Calendar should be deleted from platform

  Scenario: Verify Add/Change Google calendar functionality for client
    When Add Google calendar for client
    Then Google calendar details should display on Client's settings screen

  Scenario: Verify Change password functionality for client
    When Click on change
    And Enter Incorrect old "Kanaka@1234" and New password "Qwerty@123" and click on Submit
    Then Appropriate error message should display

  Scenario: Verify Logout functionality for coach dashboard
    When Click on Logout
    Then Login page should display


