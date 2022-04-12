from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
import allure
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")

driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("democlientuat@gmail.com")
driver.find_element_by_name("password").send_keys("Kanaka@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(5)
# #############################Home Screen ##################################
try:
    driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
    time.sleep(3)
except:
    print("No survey pending")

driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Sessions']").click()
time.sleep(5)

time.sleep(2)
mtext = driver.find_element_by_xpath(
    '//div[@aria-labelledby="netProID-tab"]').text
print(mtext)
if mtext == "You are all caught up.":
    print("Working as expected")


else:
    print("Missing survey displayed ")


time.sleep(2)
driver.find_element_by_xpath("//span[text()=' Settings']").click()
time.sleep(2)
print(driver.find_element_by_xpath('/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[2]').text)
# driver.find_element_by_xpath("(//div[text()=' 5 '])[1]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()=' Say More ']").click()
# time.sleep(5)
# driver.find_element_by_xpath("(//span[text()='No'])[1]").click()
# time.sleep(1)
# # driver.execute_script("window.scrollTo(0,500)")
# # time.sleep(5)
# element = driver.find_element_by_xpath("//td[text()='The coaching session was useful to me.']")
# driver.execute_script("return arguments[0].scrollIntoView();", element)
# time.sleep(5)
# driver.find_element_by_xpath("(//input[@value='2'])[1]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='4'])[2]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='2'])[3]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='4'])[4]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='2'])[5]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='4'])[6]").click()
# time.sleep(1)
# driver.find_element_by_xpath("(//input[@value='2'])[7]").click()
# time.sleep(2)
# driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element_by_xpath('(//label[@class="col-form-label  field-required"])[5]'))
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Excellent']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//input[@name="data[SessionValuable]"]').send_keys("Automated session is always valuable")
# time.sleep(2)
# driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
# time.sleep(5)
# successmsg = driver.find_element_by_xpath('//div[@id="toast-container"]').text
# if successmsg == "Survey data saved successfully":
#     print(successmsg)
#
# else:
#     print("error in survey")
# #
