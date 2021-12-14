Feature: Schedule a session by coach
  Scenario: Session scheduling by Ops User
    Given Operation person should logged in with valid credential "opsqdev2021@outlook.com" , "Quantuvos@123"
    When Schedule session with the client "Mabixep"
    Then Session scheduled for client and coach
