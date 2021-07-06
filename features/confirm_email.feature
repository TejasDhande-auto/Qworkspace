Feature: Send confirmation email on mail

  Scenario Outline: Confirm the email address
    Given Open browser
    When open page link from mail
    And Enter the "<email>" address
    And click on send button
    Then Confirmation email send successfully

    Examples:
      |  email  |
      |  abc@gmail.com  |
      |  xvsuwuwywiuwiwu  |
      |  tesefof795@herrain.com  |
      |  iufywhd.gmail           |

