Feature: Checking Coach's availability
  Scenario: Check whether timeslots are hiding or not
    Given : Coach should busy on next seven days at different time
    When : Client will check coach availability
    Then : If proper then display good