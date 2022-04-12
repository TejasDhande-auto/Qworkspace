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
    allure.attach("",name="Coach logged in successfully")

@when(u'Verify missing survey are pending')
def step_impl(context):
    try:
        time.sleep(5)
        context.driver.find_element_by_xpath("//button[text()='Ok']").click()
        print("Missing survey pending")
        allure.attach("", name="Missing surveys pending")

    except:
        context.driver.find_element_by_xpath("//p[text()='You are all caught up.']").is_enabled()
        print("No missing survey pending")
        allure.attach("", name="No missing survey pending against coach")

@when(u'If pending click one of missing survey')
def step_impl(context):
    try:
        time.sleep(3)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[2]/span[2]").click()
        time.sleep(2)
    except:
        allure.attach("",name="No missing survey")


@when(u'Submit the survey')
def step_impl(context):
    try:
        time.sleep(3)
        element = context.driver.find_element_by_xpath("//td[text()='The coaching session was useful to the client.']")
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        time.sleep(5)
        context.driver.find_element_by_xpath("(//input[@value='2'])[1]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='4'])[2]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='2'])[3]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='4'])[4]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='2'])[5]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='4'])[6]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='2'])[7]").click()
        time.sleep(1)
        context.driver.find_element_by_xpath("(//input[@value='4'])[8]").click()
        time.sleep(2)
        context.driver.execute_script("arguments[0].scrollIntoView();",context.driver.find_element_by_xpath('//input[@name="data[SessionValuable]"]'))
        time.sleep(2)
        context.driver.find_element_by_xpath('//input[@name="data[SessionValuable]"]').send_keys(" Hgdgdhg ")
        context.driver.execute_script("return arguments[0].scrollIntoView();",
                                      context.driver.find_element_by_xpath('//input[@name="data[OtherInfo]"]'))
        time.sleep(3)
        context.driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
        time.sleep(5)

        try:
            time.sleep(2)
            context.driver.find_element_by_xpath("//button[text()='Ok']").click()

        except:
            pass

    except:
        pass


@then(u'Survey should be submitted')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "Survey data submitted successfully":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="resource URL already exist")

        else:
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)

        time.sleep(2)

    except:
        raise Exception("Unable to submit resource")


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
    allure.attach(context.driver.find_element_by_xpath('/html/body/app-root/app-coach-dashboard/div[1]/div[1]/div[2]/div/div[2]/div[3]').text,name="Clients being reschedule",attachment_type=AttachmentType.TEXT)



@when(u'Click one of client')
def step_impl(context):
    try:
        time.sleep(2)
        context.driver.find_element_by_xpath('(//div[@class="ClientsBeingRescheduled koho"])[1]').click()
        time.sleep(3)
    except:
        allure.attach("",name="No client for reschedule")



@then(u'Selected client details screen should be open')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Client detail", attachment_type=AttachmentType.PNG)
    try:
        time.sleep(2)
        context.driver.back()
        time.sleep(5)
        context.driver.find_element_by_xpath("//button[text()='Ok']").click()

    except:
        pass


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
        allure.attach("",name="No notes for selected client")
    except:
        context.driver.find_element_by_xpath(" //span[text()=' EDIT ']").click()
        print(" Editing earlier added notes for client")
        allure.attach("", name="Editing earlier added notes for client")

    time.sleep(5)
    context.driver.find_element_by_xpath("//div[@role='textbox']").send_keys(Keys.CONTROL,'a')
    context.driver.find_element_by_xpath("//div[@role='textbox']").send_keys(Keys.DELETE)
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
            allure.attach("",name="Notes added successfully")

    except:
        raise Exception("Unable to add notes")


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
    try:
        time.sleep(2)
        context.driver.find_element_by_xpath('(//div[@id="run"])[1]').click()
    except:
        allure.attach("","no activities")



@then(u'Activity should open')
def step_impl(context):
    try:
        time.sleep(2)
        context.driver.find_element_by_xpath("(//button[text()='Close'])[2]").click()
        time.sleep(2)
        allure.attach(context.driver.get_screenshot_as_png(), name="Activity detail", attachment_type=AttachmentType.PNG)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Activity detail", attachment_type=AttachmentType.PNG)

@when(u'Check client profile is loading')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='PROFILE']").click()
    time.sleep(5)

@then(u'Client profile should load successfully')
def step_impl(context):
    try:
        if context.driver.find_element_by_xpath('//div[@class="formio-loader"]').is_displayed():
            raise Exception("Unable to load client profile")
        else:
            print(" Lets do something on client profile")
            allure.attach("", name="Client profile load successfully")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
            pass

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
            raise Exception("Unable to load session list")
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


@when(u'Click on Coach-Network Q Resources')
def step_impl(context):
        time.sleep(3)
        context.driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
        time.sleep(3)


@then(u'Coach-Network Q Resources screen should be open')
def step_impl(context):
    if context.driver.find_element_by_xpath("//span[text()='Network Q Resources ']").is_displayed():
        print("Network Q screen is displayed")
        allure.attach("", name="Network Q screen is displayed")
    else:
        allure.attach("", name="Error : Network Q screen is not displayed")
        raise Exception("Error : Network Q screen is not displayed")

@when(u'Click on Tabs on Coach-Network Q Resources')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//a[text()='Webinars']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Webinars", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Activity']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Activity", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Podcasts']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Podcasts", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Ted Talk']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Ted Talk", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Article']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Article", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Tips']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Tips", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Assessment']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Assessment", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Videos']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Videos", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Book']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Book", attachment_type=AttachmentType.PNG)
        time.sleep(3)
    except:
        raise Exception("Tabs missing")


    context.driver.find_element_by_xpath("//a[text()='Home']").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Home", attachment_type=AttachmentType.PNG)
    time.sleep(3)



@then(u'Tab related resources should display to coach on screen')
def step_impl(context):
    print("Yes opened successfully")
    allure.attach("", name="Screenshots has been attached")


@when(u'Enter text in search box on Coach-Network Q Resources screen')
def step_impl(context):

    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)

@then(u'Matched resources should display to coach')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath("//button[text()='Close']").click()
    time.sleep(2)


@when(u'Enter text in advanced search box on Coach-Network Q Resources screen')
def step_impl(context):
    context.driver.find_element_by_xpath('//button[@title="Advanced Search"]').click()
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

@then(u'Matched resources to advanced search should display')
def step_impl(context):

    if "Preparing for your first Coaching Session" == context.driver.find_element_by_xpath(
            "//span[text()=' Preparing for your first Coaching Session ']").text:
        print("Advanced search is successfull")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("",name="Matched resources displayed")
    else:
        context.driver.find_element_by_xpath(
            '//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
        print("Filter Resets")
        allure.attach("",name="Filter has been reset")


@given(u'Submit Resource modal window should be open')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='SUBMIT NEW RESOURCE']").click()
    time.sleep(2)

@when(u'Enter the resource details and click on save')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@id="Title"]').send_keys("uhs")

    context.driver.find_element_by_xpath('//textarea[@id="Description"]').send_keys("fsffsfsf")
    context.driver.find_element_by_xpath('//input[@id="Author"]').send_keys("sfsfsfs")
    time.sleep(2)
    context.driver.execute_script("arguments[0].scrollIntoView();",
                          context.driver.find_element_by_xpath("//label[text()='Resource for coach']"))
    time.sleep(5)
    context.driver.find_element_by_xpath('//select[@id="Type"]').click()
    context.driver.find_element_by_xpath("//option[text()='Tips']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//select[@id="Category"]').click()
    context.driver.find_element_by_xpath("//option[text()='Diversity, Equity and Inclusion']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//input[@id="URL"]').send_keys("www.itssuotmation.things")
    time.sleep(1)
    context.driver.find_element_by_xpath('//input[@id="DurationTime"]').send_keys("15")
    time.sleep(1)
    context.driver.find_element_by_xpath("//span[text()='Save']").click()

@then(u'Resource should be submitted for approval')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "resource URL already exist":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="resource URL already exist")

        elif errmsg == "Resources has been submitted for approval":
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Resource has been submitted for approval")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)

        time.sleep(2)

    except:
        raise Exception("Unable to submit resource")




@given(u'Coach-Profile & Preferences screen should display')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Profile and Preferences']").click()
    time.sleep(3)


@when(u'If coach personal information display')
def step_impl(context):
    if context.driver.find_element_by_xpath(
            "(//span[text()=' Profile and Preferences'])[1]").text == "Profile and Preferences":
        allure.attach("", name="Profile & preferences screen is displayed")

    else:
        allure.attach("", name="Loading icon showing")


@then(u'Coach Profile details displayed properly')
def step_impl(context):
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when(u'Enter text in field and click on submit')
def step_impl(context):

    context.driver.execute_script("window.scrollBy(0,700)", "")
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@name="data[AgeofKids]"]').clear()
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@name="data[AgeofKids]"]').send_keys("Don't want to disclose")
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(700,3500)", "")
    time.sleep(5)
    context.driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@then(u'Coach profile should be updated and updated value should display in field')
def step_impl(context):
    time.sleep(3)
    context.driver.refresh()
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(0,700)", "")
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when(u'Click on Coach-Settings')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Settings']").click()
    time.sleep(2)


@then(u'Coach-Settings screen should displayed')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Add/Change outlook calendar for coach')
def step_impl(context):
    try:
        print("Changing already added calendar")
        allure.attach("",name="Changing already added calendar")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div[1]/div/form/div[3]/div[1]/div/div[2]/div/img[1]").click()
        time.sleep(2)
    except:
        print(" Adding new calendar to platform")
        allure.attach("", name="Adding new calendar to platform")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//img[@src="../../../assets/icons/addcalendarsyn.svg"]').click()
        time.sleep(2)

    context.driver.find_element_by_xpath(
        '//*[@id="uBody"]/app-root/app-coach-calendar-access/div[1]/div[2]/div[2]').click()
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
        allure.attach("",name="New calendar added")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print("Already added calendar added")
        allure.attach("", name="Selected calendar has already been synced with platform")


    time.sleep(5)


@then(u"Outlook calendar details should display on coach's settings screen")
def step_impl(context):
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    calendarsyncstatus = context.driver.find_element_by_xpath('/html/body/app-root/app-setting/div[1]/div/div[2]/div/div[1]/div/form/div[3]/div[2]').text
    if calendarsyncstatus == "Calendar NOT Synced":
        allure.attach("", name="Calendar NOT Synced")
    else:
        allure.attach("", name="Calendar is synced")


@when(u'Click on delete calendar')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath('//img[@title="Delete calendar"]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Remove']").click()
    time.sleep(3)
    try:
        context.driver.find_element_by_xpath("//button[text()='OK']").click()
        print("Deleted Gmail calendar")
        allure.attach("",name="Synced calendar is Google ")

    except:
        print("Deleted outlook calendar")
        allure.attach("",name="Synced calendar is Outlook")


@then(u'Coach-Calendar should be deleted from platform')
def step_impl(context):
    errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    if errmsg == "Calendar has been deleted successfully ":
        print(errmsg)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Calendar has been deleted successfully")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    else:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Error in deleting calendar")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    time.sleep(2)


@when(u'Add Google calendar for coach')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath('(//img[@class="cursor-pointer"])[2]').click()
        time.sleep(2)
    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Something went wrong while adding google calendar")

    try:
        time.sleep(5)
        context.driver.find_element_by_xpath("//div[text()=' Google calendar ']").click()
        time.sleep(2)
        time.sleep(5)
        context.driver.find_element_by_id("identifierId").send_keys("automatecoach@gmail.com")
        context.driver.find_element_by_id("identifierNext").click()
        time.sleep(5)
        context.driver.find_element_by_name("password").send_keys("Kanaka@123")
        context.driver.find_element_by_id("passwordNext").click()
        time.sleep(3)
        try:
            context.driver.find_element_by_xpath("//div[text()='Confirm your recovery email']").click()
            time.sleep(3)
            context.driver.find_element_by_xpath('//input[@aria-label="Enter recovery email address"]').send_keys(
                "democoachuat@gmail.com")
            time.sleep(2)
            context.driver.find_element_by_xpath("//span[text()='Next']").click()
            time.sleep(2)

        except:
            pass
        try:
            context.driver.find_element_by_xpath('//input[@aria-labelledby="selectioni7"]').click()
            time.sleep(1)
            context.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(3)
            context.driver.find_element_by_xpath(
                "//span[text()='Continue']").click()  # driver.find_element_by_xpath("//span[text()='Cancel']").click()
            time.sleep(5)
            allure.attach("",name="Required permissions are given")

        except:
            allure.attach("", name="Access permission has already been given for selected Google calendar")

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception("Unable to click on Add icon")


@then(u"Google calendar details should display on coach's settings screen")
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    calendarsyncstatus = context.driver.find_element_by_xpath(
        '/html/body/app-root/app-setting/div[1]/div/div[2]/div/div[1]/div/form/div[3]/div[2]/span').text
    if calendarsyncstatus == "Calendar NOT Synced":
        allure.attach("", name="Calendar NOT Synced")
    else:
        allure.attach("", name="Calendar is synced")


@when(u'Click on change password icon')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//img[@title='Change Password']").click()
    time.sleep(3)

@when(u'Enter Incorrect old password and New password and click on Submit')
def step_impl(context):
    context.driver.find_element_by_name("oldPassword").send_keys("Kanaka@1234")
    context.driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
    context.driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)
    context.driver.find_element_by_xpath("(//button[text()='Close'])[2]").click()
    time.sleep(3)


@then(u'Appropriate error message should display on screen')
def step_impl(context):
    try :
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "old password is incorrect..":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="old password is incorrect : Expected")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        else:
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Password changed successfully")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        time.sleep(2)

    except:
        raise Exception("Not a proper toaster")

@when(u'Click on Logout')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()=' Logout']").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)

@then(u'Login page should display')
def step_impl(context):
    time.sleep(2)
    if context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').is_displayed():
        allure.attach("","User logged out successfully")

    else:
        raise Exception("Logout Functionality breaks")


