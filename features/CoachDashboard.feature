Feature: Verify  Coach Dashboard

  Scenario: Verify Coach login successfully
    When Login page should be open
    And Enter coach credentials "democoachuat@gmail.com" and "Kanaka@123"
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
    When Click on filter and enter "ABc" as client name
    Then Client details screen should open

  Scenario: Verify notes section under client details screen
    When Crete or edit note for client
    Then Created/edited note should display on screen

  Scenario: Verify Activities section under client details screen
    When Check activities are assigned to client
    And  click one of activity if assigned
    Then Activity should open

   Scenario: Verify Client profile section under client details screen
     When Check client profile is loading
     Then Client profile should load successfully

   Scenario: Verify Sessions section under client details screen
     When Check sessions list
     Then Session list should display

   Scenario: Verify Chat section under client details screen
     When Send message to client
     Then Message should sent

   Scenario: Check Network Q on coach Dashboard
     Given : Network Q screen on coach Dashboard should be open
     When : Check all tabs on network q screen on coach Dashboard
     And : Check Search functionality on coach Dashboard
     And : Check Advanced search Functionality on coach Dashboard
     Then : Network  Q screen on coach Dashboard should work as expected

  Scenario: Check Profile & Preferences screen on coach  dashboard
     Given : Profile & Preferences screen on coach dashboard should be open
     When : Check update preference functionality for coach
     Then : Coach Preferences should updated successfully


    Scenario: Check Add/Edit calendar functionality on Settings screen on coach dashboard
      Given : Settings screen on Coach dashboard should be open
      When : Check Add/Change calendar functionality on coach dashboard
      Then : Calendar updated succssfully

    Scenario: Check Change password functionality on Settings screen on coach dashboard
      Given : Settings screen on Coach dashboard should be open
      When : Click on change password and provide updated password
      Then : Password should be changed



