from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
import allure
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")

time.sleep(10)
driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
driver.find_element_by_name("password").send_keys("Quantuvos@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(5)
# driver.execute_script("document.body.style.zoom='90%'")
# time.sleep(5)
#############################Session Screen ##################################
# driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[2]').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[3]').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[4]').click()
# time.sleep(5)
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[1]').click()
# time.sleep(5)
# driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Scheduled")
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='View']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//span[text()='Close']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Edit']").click()
# time.sleep(2)
# driver.find_element_by_xpath(("//select[@name='status']")).click()
# time.sleep(2)
# driver.find_element_by_xpath("//option[@value='Rescheduling']").click()
# time.sleep(2)
# driver.find_element_by_xpath(("//select[@name='reason']")).click()
# time.sleep(2)
# driver.find_element_by_xpath("//option[text()='Qerror']").click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="uBody"]/modal-container/div/div/form/div[2]/textarea').send_keys("Automate change")
# time.sleep(3)
# driver.find_element_by_xpath("//button[text()='Submit']").click()
# time.sleep(5)
# driver.find_element_by_xpath('/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[5]/div[2]').click()
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[5]/div[2]').click()
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[5]/div[2]').click()
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[5]/div[2]').click()

#enabledisbalebutton depending button
status = ("Scheduled","Rescheduled","Rescheduling","Follow Up","Cancelled","Completed")
for i in range(6):

    time.sleep(5)
    driver.find_element_by_xpath('(//span[@class="ag-icon ag-icon-menu"])[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('(//input[@placeholder="Filter..."])[1]').clear()
    driver.find_element_by_xpath('(//input[@placeholder="Filter..."])[1]').send_keys(status[i])
    time.sleep(2)
    driver.find_element_by_xpath('(//div[@aria-colindex="1"])[2]').click()
    time.sleep(1)
    Current_status = status[i]
    print(Current_status)
    if driver.find_element_by_xpath("//button[text()='View']").is_enabled() and driver.find_element_by_xpath(
        "//button[text()='Edit']").is_enabled() and driver.find_element_by_xpath(
        "//button[text()='Reschedule']").is_enabled() and Current_status == "Scheduled" or Current_status =="Rescheduling" or Current_status == "Follow Up":

        print("Looks good for",status[i])

    elif driver.find_element_by_xpath("//button[text()='View']").is_enabled() and driver.find_element_by_xpath(
        "//button[text()='Edit']").is_enabled() and Current_status == "Rescheduled" :

        print("Works well for rescheduled")

    elif driver.find_element_by_xpath("//button[text()='View']").is_enabled() and Current_status == "Completed" or Current_status =="Cancelled":
        print("Looks good for",status[i])

    else:
        raise Exception
#######################################End of Session Screen ##################################

# #################################Customer Screen start############################
# driver.implicitly_wait(20)
# driver.find_element_by_xpath("//a[@title='Customers']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//button[text()='Add']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//input[@name='customerName']").send_keys("Automatecustomer")
# time.sleep(5)
# driver.find_element_by_xpath("//input[@name='PointOfContact']").send_keys("Seleniumcustomer")
# time.sleep(5)
# driver.find_element_by_xpath("//input[@name='ContactNo']").send_keys("9876543210")
# time.sleep(5)
# driver.find_element_by_name("Email").send_keys("automate@customer.com")
# time.sleep(5)
# driver.find_element_by_xpath("//select[@value='Active']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//option[text()=' Active']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Submit']").click()
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("AutomateCustomer")
# time.sleep(5)

###F###Ilter on customer screen.##################
#
# driver.find_element_by_xpath('//img[@alt="filter icon"]').click()
# time.sleep(2)
# drp1 = Select(driver.find_element_by_xpath('//select[@formcontrolname="colname"]'))
# drp1.select_by_value("b_customerName")
# time.sleep(2)
# drp2 = Select(driver.find_element_by_xpath('//select[@formcontrolname="filterType"]'))
# drp2.select_by_value("iexact")
# time.sleep(2)
# driver.find_element_by_xpath('//input[@formcontrolname="searchKey"]').send_keys("Kanaka cons pune")
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Apply']").click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input').click()
# time.sleep(2)
# ########################edit#########################
# driver.find_element_by_xpath("//button[text()='Edit']").click()
# time.sleep(5)
# driver.find_element_by_xpath('(//input[@name="PointOfContact"])[2]').clear()
# driver.find_element_by_xpath("(//input[@name='PointOfContact'])[2]").send_keys("Seleniumcustomer")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 500)")
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Submit']").click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input').click()
# time.sleep(2)
# #######################View#########################
# driver.find_element_by_xpath("//button[text()='View']").click()
# time.sleep(5)
# driver.back()
# time.sleep(5)
#############################################Onboarding################################################
# #send welcome_Individual client
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
# time.sleep(8)
# driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()
# time.sleep(10)
# driver.find_element_by_id("dropdownMenuLink").click()
# time.sleep(10)
# driver.find_element_by_id("individual-client").click()
#
# time.sleep(10)
# driver.find_element_by_name("individualclientfirstname").send_keys("IndividualAutomate")
# driver.find_element_by_name("individualclientlastname").send_keys("Client")
# driver.find_element_by_name("individualclientemail").send_keys("ffsfjhf@sjhffkh.com")
# driver.find_element_by_name("individualclientallocationhour").send_keys("55")
# time.sleep(5)
# driver.find_element_by_id("btndisable").click()
# time.sleep(5)
#
# #bulk invitation
# time.sleep(5)
# driver.find_element_by_xpath('//input[@id="file"]').send_keys("C://Users//kanaka//Downloads//CSV//Individual_Client.csv")
# time.sleep(3)
# driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
# time.sleep(5)
# try:
#     driver.find_element_by_xpath("//button[text()=' OK ']").click()
#     time.sleep(2)
# except:
#     pass
#
#
# # Customer Client
# time.sleep(10)
# driver.find_element_by_id("dropdownMenuLink").click()
# time.sleep(10)
# driver.find_element_by_id("clienttype").click()
#
# time.sleep(10)
# driver.find_element_by_name("customerclientfirstname").send_keys("CustomerAutomate")
# driver.find_element_by_name("customerclientlastname").send_keys("Client")
# driver.find_element_by_name("customerclientemail").send_keys("gfhsgj@shh.in")
# driver.find_element_by_name("customerclientallocationhour").send_keys("65")
# driver.find_element_by_name("customerclientcompanyid").send_keys("5")
# time.sleep(5)
# driver.find_element_by_id("btnsubmit").click()
# time.sleep(3)
#
# #bulk invitation
# time.sleep(5)
# driver.find_element_by_xpath('//input[@id="file"]').send_keys("C://Users//kanaka//Downloads//CSV//Customer_Client.csv")
# time.sleep(3)
# driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
# time.sleep(5)
# try:
#     driver.find_element_by_xpath("//button[text()=' OK ']").click()
#     time.sleep(2)
# except:
#     pass
#
# #coach
# time.sleep(5)
# driver.find_element_by_id("dropdownMenuLink").click()
# time.sleep(3)
# driver.find_element_by_id("coachtype").click()
# time.sleep(5)
# driver.find_element_by_name("coachfirstname").send_keys("CoachABC")
# driver.find_element_by_name("coachlastname").send_keys("XYZ")
# driver.find_element_by_name("coachemail").send_keys(Keys.CONTROL, 'v')
# time.sleep(5)
# driver.find_element_by_id("coachbtn").click()
# time.sleep(10)
#
# #bulk invitation
# time.sleep(5)
# driver.find_element_by_xpath('//input[@id="file"]').send_keys("C://Users//kanaka//Downloads//CSV//Coach.csv")
# time.sleep(3)
# driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
# time.sleep(5)
# try:
#     driver.find_element_by_xpath("//button[text()=' OK ']").click()
#     time.sleep(2)
# except:
#     pass
# #
# ################################################CLients screen#################################
# time.sleep(2)
# driver.find_element_by_xpath("(//span[text()='Clients'])[1]").click()
# time.sleep(5)
#
# ########################################Coaches#############################
# time.sleep(2)
# driver.find_element_by_xpath("(//span[text()='Coaches'])[1]").click()
# time.sleep(5)
# ##########################################Cooach selection##########################
# time.sleep(2)
# driver.find_element_by_xpath("(//span[text()='Coach Selection'])[1]").click()
# time.sleep(5)
# #####################################Main Coaches################################################
# time.sleep(2)
# driver.find_element_by_xpath("(//span[text()='Coaches'])[2]").click()
# time.sleep(10)
# driver.find_element_by_xpath("/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("QCoach1")
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Edit']").click()
# time.sleep(5)
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').clear()
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').send_keys("Automatelastname")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
# time.sleep(5)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
# time.sleep(5)
# driver.find_element_by_xpath("//a[text()=' Back']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//button[text()='Add']").click()
# time.sleep(5)
# driver.back()
# time.sleep(5)

# ################################################################Client###########################################################
# time.sleep(2)
# driver.find_element_by_xpath("(//span[text()='Clients'])[2]").click()
# time.sleep(30)
# driver.find_element_by_xpath('/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[5]/div[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("Qtestclient1")
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Edit']").click()
# time.sleep(5)
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').clear()
# driver.find_element_by_xpath('//input[@name="data[LastName]"]').send_keys("Automatelastname")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
# time.sleep(5)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
# time.sleep(5)
# driver.find_element_by_xpath("//a[text()=' Back']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//button[text()='Add']").click()
# time.sleep(5)
# driver.back()
# time.sleep(5)

#################################################Network Q resources##########################################
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()=' + Network Q']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Resources']").click()
# time.sleep(5)
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
# driver.find_element_by_xpath('//button[@title="Advanced Search"]').click()
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
# time.sleep(5)
# errmsg = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
# if errmsg == "resource URL already exist":
#     print(errmsg)
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="resource URL already exist")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#     driver.find_element_by_xpath("//span[text()='Cancel']").click()
#
# elif errmsg == "Resources has been submitted for approval":
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="Resource has been submitted for approval")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#
# else:
#     allure.attach(driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Diffrent error msg",attachment_type=AttachmentType.TEXT)
#     print(driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
#     driver.find_element_by_xpath("//span[text()='Cancel']").click()
#     raise Exception("Unable to submit resource")

# ################################################Reource Approval###########################################
# #Edit
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Resources Approval']").click()
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/app-root/app-resources-approval/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/input").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()=' Edit ']").click()
# time.sleep(5)
# driver.find_element_by_xpath('//textarea[@id="Description"]').send_keys("  extra description added by automation")
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Save']").click()
# time.sleep(5)
# errmsg1 = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
# print(errmsg1)
# if errmsg1 == "Resource details has been updated":
#     print(errmsg1)
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="Resource detail has been updated")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#
# else:
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="Resource has been submitted for approval")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#     try:
#         driver.find_element_by_xpath('//button[@aria-label="Close"]').click()
#
#     except:
#         pass
#
#
# #approved
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/app-root/app-resources-approval/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/input").click()
# time.sleep(2)
# driver.find_element_by_xpath("//button[text()='Approve']").click()
# time.sleep(2)
# time.sleep(5)
# resourceapprove = driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
# print(resourceapprove)
# if resourceapprove == "Selected resource(s) approved":
#     print(resourceapprove)
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="Resource detail has been updated")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#
# else:
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#     allure.attach("", name="Resource has been submitted for approval")
#     driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
#     driver.find_element_by_xpath('//button[@aria-label="Close"]').click()
#
# ############################################################Setttings############
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
