from Locators.locators import Locators
class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.emailaddressID = Locators.emailID
        self.passwordID = Locators.passwordID
        self.loginID = Locators.clickloginid

    def Enteremailadress(self,email):
        self.driver.find_element_by_id(self.emailaddressID).clear()
        self.driver.find_element_by_id(self.emailaddressID).send_keys(email)

    def Enterpassword(self,password):
        self.driver.find_element_by_id(self.passwordID).clear()
        self.driver.find_element_by_id(self.passwordID).send_keys(password)

    def clickonlogin(self):
        self.driver.find_element_by_id(self.loginID).click()



