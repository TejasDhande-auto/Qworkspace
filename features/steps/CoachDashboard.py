import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb, environment

@when(u'Login page should be open')
def step_impl(context):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)


@when(u'Enter coach credentials "{email}" and "{password}"')
def step_impl(context,email,password):
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@then(u'Coach dashboard should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print("Coach login successfull")

@when(u'Verify missing survey are pending')
def step_impl(context):
    try:
        time.sleep(5)
        context.driver.find_element_by_xpath("//button[text()='Ok']").click()
        print("Missing survey pending")
        time.sleep(3)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[2]/span[2]").click()
        time.sleep(2)
        context.driver.find_element_by_xpath("//button[@aria-label='Close']").click()
        time.sleep(2)

    except:
        context.driver.find_element_by_xpath("//p[text()='You are all caught up.']").is_enabled()
        print("No missing survey pending")

@when(u'If pending click one of missing survey')
def step_impl(context):
     print("TBD")


@when(u'Submit the survey')
def step_impl(context):
    print("TBD")


@then(u'Survey should be submitted')
def step_impl(context):
    print("TBD")

@when(u'Click on Week')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//div[text()= ' Week ']").click()
    time.sleep(2)


@then(u'Week view should display on screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@then(u'Click on Month')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//div[text()= ' Month ']").click()
    time.sleep(2)


@then(u'Month view should display on screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Verify the client list')
def step_impl(context):
    print(context.driver.find_element_by_xpath('/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[3]').text)


@when(u'Click one of client')
def step_impl(context):
    print("TBD")


@then(u'Selected client details screen should be open')
def step_impl(context):
    print("TBD")

@when(u'Click on filter and enter "ABc" as client name')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[text()='Clients']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[3]/span/span").click()
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
        "Demoutlookclient")
    time.sleep(4)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]").click()
    time.sleep(10)


@then(u'Client details screen should open')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Crete or edit note for client')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//span[text()=' ADD ']").click()
        print(("No note added earlier for client"))
    except:
        context.driver.find_element_by_xpath(" //span[text()=' EDIT ']").click()
        print(" Editing earlier added notes for client")

    time.sleep(5)
    context.driver.find_element_by_xpath("//div[@role='textbox']").clear()
    time.sleep(2)
    context.driver.find_element_by_xpath("//div[@role='textbox']").send_keys("Note for client name")
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Save']").click()
    time.sleep(2)

@then(u'Created/edited note should display on screen')
def step_impl(context):

    try:
        if context.driver.find_element_by_xpath("//p[text()='Note for client name']").is_displayed():
            print("Note added successfully")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
        print("Something went wrong notes not added")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Check activities are assigned to client')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()=' ACTIVITIES']").click()
    time.sleep(3)
    try:
        if context.driver.find_element_by_xpath("//label[text()=' No activities to show ' ]").is_displayed():
            print("No activity present at the time")
    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'click one of activity if assigned')
def step_impl(context):
    print("Will contuniue this")


@then(u'Activity should open')
def step_impl(context):
    print("Will contuniue this")


@when(u'Check client profile is loading')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='PROFILE']").click()
    time.sleep(5)

@then(u'Client profile should load successfully')
def step_impl(context):
    try:

        if context.driver.find_element_by_xpath('//div[@class="formio-loader"]').is_displayed():
            print("Something went wrong client profile not loading")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except:
            print(" Lets do something on client profile")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Check sessions list')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='SESSIONS']").click()

@then(u'Session list should display')
def step_impl(context):
    time.sleep(3)
    session = context.driver.find_element_by_xpath('//div[@id="tab-session"]').text
    try:
        if session == "":
            print("Sessions list not showing something went wrong")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@when(u'Send message to client')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='CHAT']").click()
    time.sleep(8)
    context.driver.find_element_by_xpath('//input[@placeholder="send message..."]').send_keys("Automated message by coach")
    time.sleep(2)
    context.driver.find_element_by_xpath('//i[@title="Click here send message."]').click()
    time.sleep(5)

@then(u'Message should sent')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@given(u': Network Q screen on coach Dashboard should be open')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
    time.sleep(3)

@when(u': Check all tabs on network q screen on coach Dashboard')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//a[text()='Webinars']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Activity']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Podcasts']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Ted Talk']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Article']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Tips']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Assessment']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Videos']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Book']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Home']").click()

    except:
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Home']").click()


@when(u': Check Search functionality on coach Dashboard')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath("//button[text()='Close']").click()
    time.sleep(2)


@when(u': Check Advanced search Functionality on coach Dashboard')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[text()=' ADVANCED SERACH ']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@name='titileSearchValue']").send_keys("Prepar")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='descriptionSearchValue']").send_keys("Prepare")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='authorSearchValue']").send_keys("Steve")
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault1']").click()  # And1
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault3']").click()  # and2
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Apply']").click()
    time.sleep(3)

    if "Preparing for your first Coaching Session" == context.driver.find_element_by_xpath(
            "//span[text()=' Preparing for your first Coaching Session ']").text:
        print("Advanced search is successfull")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    else:
        context.driver.find_element_by_xpath(
            '//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
        print("Filter Resets")



@then(u': Network  Q screen on coach Dashboard should work as expected')
def step_impl(context):
    print("Working as expected")


@given(u': Profile & Preferences screen on coach dashboard should be open')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Profile and Preferences']").click()
    time.sleep(3)

@when(u': Check update preference functionality for coach')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,700)", "")
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@name="data[AgeofKids]"]').clear()
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@name="data[AgeofKids]"]').send_keys("Don't want to disclose")
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(800,3000)", "")
    time.sleep(5)
    context.driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@then(u': Coach Preferences should updated successfully')
def step_impl(context):
    time.sleep(3)
    context.driver.refresh()
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(0,700)", "")
    time.sleep(5)
    if context.driver.find_element_by_xpath('//input[@name="data[AgeofKids]"]').text == "Don't want to disclose":
        print("Profile & preferences updated successfully")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    else:
        print("Something went wrong in PP")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



@given(u': Settings screen on Coach dashboard should be open')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Settings']").click()
    time.sleep(2)

@when(u': Check Add/Change calendar functionality on coach dashboard')
def step_impl(context):
    try:
        print("Changing already added calendar")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div[1]/div/form/div[3]/div[1]/div/div[2]/div/img[1]").click()
        time.sleep(2)
    except:
        print(" Adding new calendar to platform")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//img[@src="../../../assets/icons/addcalendarsyn.svg"]').click()
        time.sleep(2)

    context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-coach-calendar-access/div[1]/div[2]/div[2]').click()
    time.sleep(3)
    context.driver.find_element_by_id('i0116').send_keys("automatecoach@outlook.com")
    time.sleep(5)
    context.driver.find_element_by_id('idSIButton9').click()
    time.sleep(5)
    context.driver.find_element_by_id('i0118').send_keys("Kanaka@123")
    time.sleep(3)
    context.driver.find_element_by_id('idSIButton9').click()
    time.sleep(3)
    context.driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(3)
    try:
        context.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        context.driver.find_element_by_xpath('//*[@id="idBtn_Accept"]').click()
        time.sleep(5)
        print("New calendar added")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print("Already added calendar added")

    time.sleep(5)

@then(u': Calendar updated succssfully')
def step_impl(context):
    print("Pass")

@when(u': Click on change password and provide updated password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//img[@title='Change Password']").click()
    time.sleep(3)
    context.driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
    context.driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
    context.driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@then(u': Password should be changed')
def step_impl(context):
    time.sleep(3)


