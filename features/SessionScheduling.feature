Feature: Session scheduling across all 3 three user roles
    Scenario: Session scheduling by client
    Given Client should logged in with valid credential "qtestclient+1@gmail.com" , "Qwerty@123"
    When Schedule Session with coach
    Then First session should be scheduled


    Scenario: Session scheduling by coach
    Given Coach should logged in with valid credential "qtestcoach+1@gmail.com" , "Qwerty@123"
    When Schedule session with client "QtestClient1"
    Then Session scheduled with client


    Scenario: Session scheduling by Ops User
    Given Operation person should logged in with valid credential "opsqdev@outlook.com" , "Quantuvos@123"
    When Schedule session with the client "QtestClient1"
    Then Session scheduled for client and coach