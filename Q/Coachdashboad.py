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



driver.find_element_by_name("email").send_keys("democoachuat@gmail.com")
driver.find_element_by_name("password").send_keys("Kanaka@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(10)
# #############################Home Screen ##################################
try:
    time.sleep(5)
    driver.find_element_by_xpath("//button[text()='Ok']").click()
    # print("Missing survey pending")
    # time.sleep(3)
    # driver.find_element_by_xpath("/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[2]/span[2]").click()
    # time.sleep(5)
    # # driver.find_element_by_xpath("//button[@aria-label='Close']").click()
    # # time.sleep(2)
    # element = driver.find_element_by_xpath("//td[text()='The coaching session was useful to the client.']")
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
    # time.sleep(1)
    # driver.find_element_by_xpath("(//input[@value='4'])[8]").click()
    # time.sleep(2)
    # driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath('//input[@name="data[SessionValuable]"]'))
    # time.sleep(2)
    # driver.find_element_by_xpath('//input[@name="data[SessionValuable]"]').send_keys(" Hgdgdhg ")
    # driver.execute_script("return arguments[0].scrollIntoView();",
    #                               driver.find_element_by_xpath('//input[@name="data[OtherInfo]"]'))
    # time.sleep(3)
    # driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
    # time.sleep(5)



except:
    driver.find_element_by_xpath("//p[text()='You are all caught up.']").is_enabled()
    print("No missing survey pending")
# # #client being reschedule
# print(driver.find_element_by_xpath('/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[3]').text)
#
# driver.find_element_by_xpath("//div[text()= ' Month ']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[text()= ' Week ']").click()
# time.sleep(2)
# # driver.find_element_by_xpath('//span[@class="m-l-02 event-text"]').click()
# # time.sleep(3)
# # driver.find_element_by_xpath("//span[text()='Close']").click()
# # time.sleep(5)
#
# #----------------------------------------Clients---------------------------------
# driver.find_element_by_xpath("//span[text()='Clients']").click()
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[3]/span/span").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("Demoutlookclient")
# time.sleep(4)
# driver.find_element_by_xpath(
#         "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]").click()
# time.sleep(10)

# # Note for Client
# try:
#     driver.find_element_by_xpath("//span[text()=' ADD ']").click()
#     print(("No note added earlier for client"))
# except:
#     driver.find_element_by_xpath(" //span[text()=' EDIT ']").click()
#     print(" Editing earlier added notes for client")
#
# time.sleep(5)
# driver.find_element_by_xpath("//div[@role='textbox']").send_keys("Note for client name")
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Save']").click()
# time.sleep(2)
#
# try:
#     if driver.find_element_by_xpath("//p[text()='Note for client name']").is_displayed():
#         print("Note added successfully")
#
# except:
#     print("Something went wrong notes not added")
#
# #
# #Activities
# time.sleep(2)
# driver.find_element_by_xpath("//a[text()=' ACTIVITIES']").click()
# time.sleep(3)
# if driver.find_element_by_xpath("//label[text()=' No activities to show ' ]").is_displayed():
#     print("No activity present at the time")
# else:
#     print(" Lets see toward activities")
#
# driver.find_element_by_xpath("//span[text()=' ADD ']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//input[@id='myInput']").send_keys("prepa")
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="run"]/h6').click()
# time.sleep(3)
# driver.find_element_by_xpath('(//input[@type="checkbox"])[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Ok']").click()
# time.sleep(3)
# driver.find_element_by_xpath("(//button[text()='Ok'])[2]").click()
#
# toastmsg = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
# if toastmsg == "Activity already exists":
#     print("Exit already")
#
# else:
#     print(toastmsg)

# # #Client Profile
# time.sleep(2)
# driver.find_element_by_xpath("//a[text()='PROFILE']").click()
# time.sleep(5)
#
# if driver.find_element_by_xpath('//div[@class="formio-loader"]').is_displayed():
#     raise Exception("Unable to load client profile")
#     print("Something went wrong client profile not loading")
#
# else:
#     print(" Lets do something on client profile")

# # #Sessions
# time.sleep(2)
# driver.find_element_by_xpath("//a[text()='SESSIONS']").click()
# time.sleep(3)
# session = driver.find_element_by_xpath('//div[@id="tab-session"]').text
# if session == "":
#     print("Sessions list not showing something went wrong")
#
#
# # #CHAT
# time.sleep(2)
# driver.find_element_by_xpath("//a[text()='CHAT']").click()
# time.sleep(8)
# driver.find_element_by_xpath('//input[@placeholder="send message..."]').send_keys("Automated message by coach")
# time.sleep(2)
# driver.find_element_by_xpath('//i[@title="Click here send message."]').click()
# time.sleep(5)
#
# #-----------------------------------Network Q----------------------------
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
# time.sleep(3)
# try:
#     driver.find_element_by_xpath("//a[text()='Webinars']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Activity']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Podcasts']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Ted Talk']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Article']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Tips']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Assessment']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Videos']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Book']").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Home']").click()
#
# except:
#     time.sleep(3)
#     driver.find_element_by_xpath("//a[text()='Home']").click()
#
# # #Search by title Functionality
# time.sleep(3)
# driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="run"]/h6').click()
# time.sleep(3)
# driver.find_element_by_xpath("//button[text()='Close']").click()
# time.sleep(2)
# #Advanced Search
# driver.find_element_by_xpath("//span[text()=' ADVANCED SERACH ']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//input[@name='titileSearchValue']").send_keys("Prepar")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@name='descriptionSearchValue']").send_keys("Prepare")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@name='authorSearchValue']").send_keys("Steve")
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='flexRadioDefault1']").click()  #And1
# driver.find_element_by_xpath("//*[@id='flexRadioDefault3']").click()  #and2
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Apply']").click()
# time.sleep(3)
#
# if "Preparing for your first Coaching Session" == driver.find_element_by_xpath("//span[text()=' Preparing for your first Coaching Session ']").text:
#     print("Advanced search is successfull")
# else:
#     driver.find_element_by_xpath('//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
#     print("Filter Resets")
#
# #submit new resources
# driver.find_element_by_xpath("//span[text()='SUBMIT NEW RESOURCE']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//input[@id="Title"]').send_keys("uhs")
#
# driver.find_element_by_xpath('//textarea[@id="Description"]').send_keys("fsffsfsf")
# driver.find_element_by_xpath('//input[@id="Author"]').send_keys("sfsfsfs")
# time.sleep(2)
# driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath("//label[text()='Resource for coach']"))
# time.sleep(5)
# driver.find_element_by_xpath('//select[@id="Type"]').click()
# driver.find_element_by_xpath("//option[text()='Tips']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//select[@id="Category"]').click()
# driver.find_element_by_xpath("//option[text()='Diversity, Equity and Inclusion']").click()
# time.sleep(1)
# driver.find_element_by_xpath('//input[@id="URL"]').send_keys("www.itssureffgdfotmatdion.things")
# time.sleep(1)
# driver.find_element_by_xpath('//input[@id="DurationTime"]').send_keys("15")
# time.sleep(1)
# driver.find_element_by_xpath("//span[text()='Save']").click()
#
# try:
#     errmsg = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
#     if errmsg == "resource URL already exist":
#         print(errmsg)
#         allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#         allure.attach("", name="resource URL already exist")
#         driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#
#     elif errmsg == "Resources has been submitted for approval":
#         allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#         allure.attach("", name="Resource has been submitted for approval")
#         driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#
#     else:
#         allure.attach(driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Diffrent error msg",attachment_type=AttachmentType.TEXT)
#         print(driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
#
#     time.sleep(2)
#
# except:
#     raise Exception("Unable to submit resource")
# #-------------------------Profile and preferences----------------------------
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Profile and Preferences']").click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,600)", "")
# time.sleep(5)
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').clear()
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').send_keys("Don't want to disclose")
# time.sleep(3)
# driver.execute_script("window.scrollBy(600,3000)", "")
# time.sleep(5)
# driver.find_element_by_xpath('//button[@type="submit"]').click()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# # driver.execute_script("window.scrollBy(0,600)", "")
# # time.sleep(5)
# # driver.find_element_by_xpath('//input[@name="data[LastName]"]').click()
# # time.sleep(2)
# text1 = driver.find_element_by_xpath('//input[@name="data[LastName]"]').text
# print(text1)
# if text1 == "Don't want to disclose":
#     print("Profile & preferences updated successfully")
# else:
#     print("Something went wrong in PP")

#
#------------------------------------------------Settings-----------------------------
time.sleep(3)
driver.find_element_by_xpath("//span[text()=' Settings']").click()
time.sleep(2)
driver.find_element_by_xpath("//img[@title='Change Password']").click()
time.sleep(3)
driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Submit']").click()
time.sleep(2)

#add calendar
try:
    print("Changing already added calendar")
    driver.find_element_by_xpath("/html/body/app-root/app-setting/div[1]/div/div[2]/div/div[1]/div/form/div[3]/div[1]/div/div[2]/div/img[1]").click()
    time.sleep(2)
except:
    print(" Adding new calendar to platform")
    driver.find_element_by_xpath('//img[@src="../../../assets/icons/addcalendarsyn.svg"]').click()
    time.sleep(2)

driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-coach-calendar-access/div[1]/div[2]/div[2]').click()
time.sleep(3)
driver.find_element_by_id('i0116').send_keys("automatecoach@outlook.com")
time.sleep(5)
driver.find_element_by_id('idSIButton9').click()
time.sleep(5)
driver.find_element_by_id('i0118').send_keys("Kanaka@123")
time.sleep(3)
driver.find_element_by_id('idSIButton9').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="idBtn_Accept"]').click()
time.sleep(2)

#
#
#
#
#
#
#
#
#
