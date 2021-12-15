Feature: Session scheduling across all 3 three user roles
    Scenario: Session scheduling by client
    Given Client should logged in with valid credential "mabixep475@gyn5.com" , "Qwerty@123"
    When Schedule Session with coach
    Then First session should be scheduled


    Scenario: Session scheduling by coach
    Given Coach should logged in with valid credential "yemefis666@keagenan.com" , "Qwerty@123"
    When Schedule session with client "Mabixep"
    Then Session scheduled with client


    Scenario: Session scheduling by Ops User
    Given Operation person should logged in with valid credential "opsqdev2021@outlook.com" , "Quantuvos@123"
    When Schedule session with the client "Mabixep"
    Then Session scheduled for client and coach