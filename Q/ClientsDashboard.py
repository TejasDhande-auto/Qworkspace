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
# # #Next Session
# if driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").is_enabled():
#     sessiontime =  driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/label/span').text
#     print(sessiontime)
#     print("Join session button is disabled")
# else:
#     driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").click()
#     print("Session details showed")
#
# #Coaching Goals
# time.sleep(5)
# try:
#     driver.find_element_by_xpath("//span[text()=' ADD']").click()
# except:
#     print("Notes already added")
#     driver.find_element_by_xpath("//span[text()='EDIT']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.DELETE)
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys("My Goals")
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()
#
# text1 = driver.find_element_by_xpath('//*[@id="coachingGoals-Parent"]/div/div[2]/ul/li/p').text
# if text1 == "My Goals":
#     print("Goals adeed successfully")
#
# else:
#     print(" Not able to add goal")
#
# #scenario2
# driver.find_element_by_xpath("//span[text()='EDIT']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.DELETE)
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()
# time.sleep(2)
# text1 = driver.find_element_by_xpath("//span[text()=' ADD']").text
# if text1 == "ADD":
#     print("Goals has been deleted successfully")
#
# else:
#     print("Something went wrong goals not deleted")


#  #Activities
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='ACTIVE']").click()
# time.sleep(5)
# try:
#     element = driver.find_element_by_xpath('/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
#     driver.execute_script("return arguments[0].scrollIntoView();", element)
#     #print("Only self activities are here")
#
# except:
#     element= driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
#     driver.execute_script("return arguments[0].scrollIntoView();", element)
#     #print("Only coach activities are here")
#
# time.sleep(5)
# driver.find_element_by_xpath("//span[text()='ARCHIVED']").click()
# time.sleep(4)
# try:
#     element = driver.find_element_by_xpath('/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
#     driver.execute_script("return arguments[0].scrollIntoView();", element)
#     #print("Only self activities are here")
#
# except:
#     element = driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
#     driver.execute_script("return arguments[0].scrollIntoView();", element)
#     #print("Only coach activities are here")
#
# time.sleep(8)
# driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/a/img').click()
# time.sleep(5)
# if " Activities" == driver.find_element_by_xpath("//span[text()=' Activities']").text:
#      print("Navigated to Activities page successfully")
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Home']").click()
# time.sleep(3)


# #Recommended on Network

# driver.find_element_by_xpath('/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/label/span').click()
# time.sleep(2)
# #driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[1]/img').click() #open
# driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[2]').click()# Close
# time.sleep(5)
#
# element = driver.find_element_by_xpath("/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[6]/div/div[2]")
# driver.execute_script("return arguments[0].scrollIntoView();", element)
# time.sleep(10)
#
# driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/a/img').click()
# time.sleep(5)
# if "Network Q Resources" == driver.find_element_by_xpath("//span[text()='Network Q Resources ']").text:
#     print("Navigated to Network Q successfully")
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Home']").click()
# time.sleep(3)


#
# #chat
# driver.find_element_by_xpath("//input[@placeholder='send message...']").send_keys("Hii Automated message from client")
# driver.find_element_by_xpath("//i[@title='Click here send message.']").click()
# time.sleep(10)
#Screenshot required to verify

#send file not work need to
# uploadfile = driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[2]/app-chat/div/div/div[3]/button[2]/i')
# time.sleep(5)
# uploadfile.send_keys("D://backup kanaka//kanaka new//kanaka new//desktop//Aug//1//ClientDashboard.png")

############################################# Network Q Resouces#################################
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
time.sleep(3)
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

#Search by title Functionality
time.sleep(3)
driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="run"]/h6').click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='checkbox']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()
time.sleep(2)
errmsg = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
print(errmsg)
#Advanced Search
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


########################################### Sessions#######################
# driver.implicitly_wait(10)
# driver.find_element_by_xpath("//span[text()='Sessions']").click()
# time.sleep(5)
#
# text1 = driver.find_element_by_xpath("//a[@class='nav-link font-size-9 koho active-tab-color']").text
# if text1 == "NOTES":
#     print("No Missing survey")
# elif text1 == "ACTIVITIES":
#     print("Error occurred activities default selected")
# else:
#     print("Missing survey are pending")
#     driver.find_element_by_xpath("//a[text()='NOTES']").click()
#
# if driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").is_displayed():
#     print("Notes are available for current month")
#     print(driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
#     action = ActionChains(driver)
#     action.move_to_element(driver.find_element_by_xpath("//span[text()=' Tuesday, February 8, 2022 ']")).move_to_element(driver.find_element_by_xpath("//img[@popover='Edit']")).click().perform()
#     time.sleep(5)
#     driver.find_element_by_xpath('//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').send_keys("My Automated Notes")
#     time.sleep(2)
#     driver.find_element_by_xpath("//span[text()='Save']").click()
#     time.sleep(2)
#
#
# time.sleep(5)
# driver.find_element_by_xpath("//a[text()='ACTIVITIES']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//input[@id='assignmentCheckBox-0-0']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='No']").click()
# time.sleep(1)


###################ACTIVITIES#################################
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Activities']").click()
# time.sleep(5)
# text2 = driver.find_element_by_xpath("//a[@class='navanchor border-radius-4 nav-link koho font-weight-500 font-size-9 align-items-center active-tab-color']").text
# if text2 == "Active":
#     print("Working as expected")
# else:
#     print("Something went wrong")
#
# driver.find_element_by_xpath("//a[text()='ADD']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="run"]/h6').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="Preparing for your first Coaching Session"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()
# time.sleep(3)
# driver.back()
# time.sleep(2)
# driver.find_element_by_xpath("//a[text()='Archived']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Preparing for your first Coaching Session ']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='staticModal']/div/div/div[3]/button[2]").click()
# time.sleep(2)

####################################################### P & P ##########################
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()=' Profile and Preferences']").click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,800)", "")
# time.sleep(5)
# driver.find_element_by_name("data[ReferralName]").send_keys("Kanaka Software")
# time.sleep(3)
# driver.execute_script("window.scrollBy(800,1700)", "")
# time.sleep(2)
# driver.find_element_by_xpath("//button[@name='data[submit]']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Activities']").click()
# driver.find_element_by_xpath("//span[text()=' Profile and Preferences']").click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,800)", "")
# time.sleep(5)
# print(driver.find_element_by_name("data[ReferralName]").text)
# if driver.find_element_by_name("data[ReferralName]").text == "Kanaka Software":
#     print("Profile & preferences updated successfully")
# else:
#     print("Something went wrong in PP")

############################Settings#######################################################
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()=' Settings']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//img[@title='Change Password']").click()
# time.sleep(3)
# driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
# driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
# driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
# time.sleep(3)
# driver.find_element_by_xpath("//button[text()='Submit']").click()
# time.sleep(2)

#add calendar
# try:
#     driver.find_element_by_xpath("/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div/div[1]").click()
#     time.sleep(2)
# except:
#     driver.find_element_by_xpath("/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div/img").click()
#     time.sleep(2)
#
# driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-coach-calendar-access/div[1]/div[2]/div[2]').click()
# time.sleep(3)
# driver.find_element_by_id('i0116').send_keys("automatecoach@outlook.com")
# time.sleep(5)
# driver.find_element_by_id('idSIButton9').click()
# time.sleep(5)
# driver.find_element_by_id('i0118').send_keys("Kanaka@123")
# time.sleep(3)
# driver.find_element_by_id('idSIButton9').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
# time.sleep(3)
# driver.execute_script("window.scrollTo(0, 500)")
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="idBtn_Accept"]').click()
# time.sleep(2)




