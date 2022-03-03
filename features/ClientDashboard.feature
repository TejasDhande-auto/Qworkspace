Feature: Check Client Dashboard Functionality
  Scenario: Check Home screen on Client Dashboard
    Given : Client should login into system with "democlientuat@gmail.com" and "Kanaka@123" credentials
    When : Check Next session is scheduled or not
    And : Check Coaching Goals functionality
    And : Check activities section
    And : Check recommeneded on network q functionality
    And : Check Chat Functionality
    Then : Client dashboard- Home screen should work as expected

   Scenario: Check Network Q on client Dashboard
     Given : Network Q screen should be open
     When : Check all tabs on network q screen
     And : Check Search functionality
     And : Check Advanced search Functionality
     Then : Network  Q screen should work as expected

   Scenario: Check Session screen on Client Dashboard
     Given : Session screen should be open
     When : Check Notes section in session screen
     And : Check Activites section on session screen
     And : Check missing survey section on session screen
     And : Check session scheduling functionality
     Then : Sessions screen should work as expected


   Scenario: Check Activities screen on Client Dashboard
     Given : Activities screen should be open
     When : Check active activities section
     And : Check Add self activity functionality
     And : Check archived activities section
     Then : Activities screen should work as expected


   Scenario: Check Profile & Preferences screen on client dashboard
     Given : Profile & Preferences screen should be open
     When : Check update preference functionality
     Then : Preferences should updated successfully


    Scenario: Check Settings screen on client dashboard
      Given : Settings screen should be open
      When : Check Add/Change calendar functionality
      And : Check Change password functionality
      Then : Both test cases should pass
