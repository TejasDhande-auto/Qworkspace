Feature: Verify Operation Dashboard functionality

  Scenario: Verify Ops login functionality
    When Login page should be open
    And Enter Ops credentials "opsqdev@outlook.com" and "Kanaka@123"
    Then Operation dashboard should display

    Scenario: Verify enabling/disabling of buttons based on session selected
    When Select session
    Then Related buttons should enable

  Scenario: Verify Upcoming session filter on Sessions screen
    Given Sessions screen should be open
    When Click on dropdown and select next 10 days
    Then Sessions in next 10 days should display
    When Click on dropdown and select next 20 days
    Then Sessions in next 20 days should display
    When Click on dropdown and select next 30 days
    Then Sessions in next 30 days should display
    When Click on dropdown and select All option
    Then All Sessions details should display

  Scenario: Verify Search functionality on sessions screen
    When Type "Scheduled" in search box
    Then Matched results should display

  Scenario: Verify View functionality on sessions screen
    When select one session and click on view
    Then Session detail should display

  Scenario: Verify Edit functionality on sessions screen
    When select one session and click on edit
    And Edit the session status and reason
    Then Selected session should get updated

  Scenario: Verify Customers screen is displayed
    When Click on Customers
    Then Customers screen should get opened

  Scenario: Verify Add customer functionality
    When Click on Add, enter customer details and click on submit
    Then Customers should get added to platform

  Scenario: Verify the edit customer details functionality
    When Click on Edit, edit details and click on submit
    Then Customer details should get updated in platform

  Scenario: Verify Advanced filter functioality
    When Click on filter and apply filter
    Then Matched customers should display on screen

  Scenario: Verify View functionality on customers screen
    When Select one of customer and click on View
    Then Customer specific client should display on clients screen

  Scenario: Verify send email invitation functionality to individual client
    Given Send Welcome screen should be open and Individual client should be selected
    When Enter individual-client details and click on submit
    Then Appropriate message should display (Individual client)

  Scenario: Verify send Bulk email invitation functionality individual-client
    When Upload individual.csv file and click on Submit
    Then Appropriate message should display (Bulk Individual clients)

  Scenario: Verify send email invitation functionality to customer client
    Given Send Welcome screen should be open and customer client should be selected
    When Enter customer-client details and click on submit
    Then Appropriate message should display (Customer client)

  Scenario: Verify send Bulk email invitation functionality Customer-client
    When Upload customerclient.csv file and click on Submit
    Then Appropriate message should display (Bulk Customer clients)

  Scenario: Verify send email invitation functionality to Coach
    Given Send Welcome screen should be open and Coach should be selected
    When Enter Coach details and click on submit
    Then Appropriate message should display (Coach)

  Scenario: Verify send Bulk email invitation functionality Coach
    When Upload Coach.csv file and click on Submit
    Then Appropriate message should display (Bulk Coach)

  Scenario: Verify Onboarding-Clients screen is displayed
    When Click on Onboarding-Clients screen
    Then Onboarding-Clients screen should display

  Scenario: Verify Onboarding-Coaches screen is displayed
    When Click on Onboarding-Coaches screen
    Then Onboarding-Coaches screen should display

  Scenario: Verify Onboarding-Coach selection screen is displayed
    When Click on Onboarding-Coach selection screen
    Then Onboarding-Coach selection screen should display


  Scenario: Verify Coaches screen on ops dashboard is displayed
    When Click on Coaches on ops dashboard screen
    Then Coaches screen on ops dashboard should display

  Scenario: Verify Coach detail edit functionality on Coaches screen
    When Select one coach and click on edit
    And Edit the details of Coaches
    Then Coach details should get updated by ops user

  Scenario: Verify Add Coach functionality on Coaches screen
    When Click Add button on Coaches screen
    Then Coach invitation screen should be open


  Scenario: Verify Clients screen on ops dashboard is displayed
    When Click on Clients on ops dashboard screen
    Then Clients screen on ops dashboard should display

  Scenario: Verify Client detail edit functionality on client screen
    When Select one client and click on edit
    And Edit the details of client
    Then Client details should get updated by ops user

  Scenario: Verify Session scheduling functionality
    When Select client "Qtestclient1" and Click Schedule session button
    Then Next session calendar should display to ops user
    When Ops user select available date and time and click on save
    Then Session should be scheduled for client and coach

  Scenario: Verify Add Client functionality on client screen
    When Click Add button on clients screen
    Then Individual client invitation screen should be open


  Scenario: Verify Ops-Network Q Resources screen is displayed
    When  Click on Ops-Network Q Resources
    Then  Ops-Network Q Resources screen should be open

  Scenario: Verify Tab switching on Ops-Network Q Resources screen
    When Click on Tabs on Ops-Network Q Resources
    Then Tab related resources should display to Ops on screen

  Scenario: Verify Search functionality on Ops-Network Q Resources screen
    When Enter text in search box on Ops-Network Q Resources screen
    Then Matched resources should display to Ops

  Scenario: Verify Advanced search functionality on Ops-Network Q Resources screen
    When Enter text in advanced search box on Ops-Network Q Resources screen
    Then Matched resources to advanced search should display on Ops-Network Q

  Scenario: Verify Submit Resource functionality on Ops-Network Q Resources screen
    Given Submit Resource modal window should be open on Ops-Network Q Resources screen
    When Enter the resource details and click on save Ops-Network Q Resources screen
    Then Resource created by ops user should be submitted for approval

  Scenario: Verify Resources Approval is displayed
    When Click on Resources Approval
    Then Resources approval screen should display

  Scenario: Verify Edit resource functionality
    When Select on resource and edit the resource details
    Then Resouce details should be updated

  Scenario: Verify Approve functionality
    When Select one of resource and click on approve
    Then Resource should be approved

  Scenario: Verify Ops-Settings screen is displayed
    When Click on Ops-Settings
    Then Ops-Settings screen should displayed

  Scenario: Verify Change password functionality for ops
    When Click on change password icon on ops-settings screen
    And Enter Incorrect old password and New password of ops and click on Submit
    Then Appropriate error message should display on ops-settings screen

  Scenario: Verify Logout functionality for Ops dashboard
    When Click Logout on ops dashboard
    Then Login page should be displayed