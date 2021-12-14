Feature: Checking Outlook Coach's availability
  Scenario: Check whether timeslots are hiding or not
    Given : Outlook Coach should busy on next seven days at different time login as "automatecoach@outlook.com","Kanaka@123"
    When : Client will check coach availability by login as "lalolac598@iistoria.com","Kanaka@123"
    Then : If proper then display better