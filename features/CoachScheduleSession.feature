Feature: Schedule a session by coach
  Scenario: Session scheduling by coach
    Given Coach should logged in with valid credential "yemefis666@keagenan.com" , "Qwerty@123"
    When Schedule session with client "Mabixep"
    Then Session scheduled with client
