from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver

import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://myaccount.google.com/u/2/permissions")


time.sleep(5)
driver.find_element_by_id("identifierId").send_keys("automatecoach@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys("Kanaka@123")
driver.find_element_by_id("passwordNext").click()
time.sleep(3)

try:
    driver.find_element_by_xpath("(//div[text()='Quantuvos'])[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("(//span[text()='Remove access'])[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("(//span[text()='OK'])[2]").click()

except:
    pass

print("Calendar access already been removed")
print("You haven’t given any apps or services permission to access your Google Account")
