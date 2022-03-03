Feature: Session scheduling across all 3 three user roles
    Scenario: Session scheduling by client
    Given Client should logged in with valid credential "vapop83802@datakop.com" , "Qwerty@123"
    When Schedule Session with coach
    Then First session should be scheduled


    Scenario: Session scheduling by coach
    Given Coach should logged in with valid credential "democoachuat@gmail.com" , "Kanaka@123"
    When Schedule session with client "Vapop"
    Then Session scheduled with client


    Scenario: Session scheduling by Ops User
    Given Operation person should logged in with valid credential "opsuat2021@outlook.com" , "Quantuvos@123"
    When Schedule session with the client "Vapop"
    Then Session scheduled for client and coach