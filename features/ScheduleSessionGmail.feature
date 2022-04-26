Feature: Checking Coach's availability
  Scenario: Check whether timeslots are hiding or not
    Given : Coach should busy on next seven days at different time by login as  "kcalendartest@gmail.com" and "Kanaka@123"
    When : Client will check coach availability by login as "cahoyo3533@shirulo.com","Kanaka@123"
    Then : If proper then display good