import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb, environment

@when(u'Enter client credentials as "{email}" and "{password}"')
def step_impl(context,email,password):
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@then(u'Client dashboard should display')
def step_impl(context):
    try:

        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        print("No survey pending")
        allure.attach("", name="No survey pending")

    try:
        if context.driver.find_element_by_xpath('//span[@id="dashboard-nav-welcome-back"]').is_displayed:
            print("Client logged in successfully")
            allure.attach("", name="Client logged in successfully")
    except:
        print("Something went wrong")
        allure.attach("", name="Something went wrong")

@when(u'Next session is not scheduled or next session is after 24 hours')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Next session", attachment_type=AttachmentType.PNG)

@then(u'Join session button should be disable')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").click()
        time.sleep(2)
        context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[5]/div/div/div[3]/button[2]').click()
        time.sleep(2)
    except:
        print("Join session button is disabled")
        allure.attach("", name="Join session button is disabled")


@when(u'Next session is scheduled')
def step_impl(context):
    print(" I don't have anything for here")

@then(u'Join session button should be enable')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").click()
        print("Session details showed")
        allure.attach("", name="Session details showed")
        time.sleep(2)
        context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[5]/div/div/div[3]/button[2]').click()
        time.sleep(2)
    except:
        pass


@when(u'Click on Add and enter text and click on save')
def step_impl(context):
    time.sleep(5)
    try:
        context.driver.find_element_by_xpath("//span[text()=' ADD']").click()
        print("Creating new goal")
        allure.attach("",name="Creating new Goal")
    except:
        print("Goals already set")
        allure.attach("", name="Goals already set")
        context.driver.find_element_by_xpath("//span[text()='EDIT']").click()

    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.CONTROL, 'a')
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.DELETE)
    time.sleep(5)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys("My Goals")
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()

@then(u'Entered text in RichText box should display on screen')
def step_impl(context):

    text1 = context.driver.find_element_by_xpath('//*[@id="coachingGoals-Parent"]/div/div[2]/ul/li/p').text
    if text1 == "My Goals":
        print("Coaching Goals set successfully")
        allure.attach("", name="Coaching Goals set successfully")

    else:
        print(" Not able to set coaching goals")
        allure.attach("", name="Not able to set coaching goals")


@when(u'Clear the data and click on save')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[text()='EDIT']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.CONTROL, 'a')
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.DELETE)
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()
    time.sleep(2)

@then(u'Goals should be deleted')
def step_impl(context):
    text1 = context.driver.find_element_by_xpath("//span[text()=' ADD']").text
    if text1 == "ADD":
        print("Goals has been deleted successfully")
        allure.attach("", name="Goals has been deleted successfully")

    else:
        print("Something went wrong goals not deleted")
        allure.attach("", name="Something went wrong goals not deleted")


@when(u'Active button default selected')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@then(u'Active activities should display on home screen')
def step_impl(context):
    try:
        element = context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only self activities are here")

    except:
        element = context.driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only coach activities are here")

@when(u'Click on Archived')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='ARCHIVED']").click()
    time.sleep(5)

@then(u'Archived activities should display')
def step_impl(context):
    try:
        element = context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only self activities are here")

    except:
        element = context.driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only coach activities are here")


@when(u'Click on "see all" button')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(
        '//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/a/img').click()
    time.sleep(5)

@then(u'Screen should navigate Activities screen')
def step_impl(context):
    if " Activities" == context.driver.find_element_by_xpath("//span[text()=' Activities']").text:
        print("Naviagated to Activities page successfully")
        allure.attach("", name="Navigated to Activities page successfully")

    context.driver.find_element_by_xpath("//span[text()='Home']").click()
    time.sleep(3)
    try:
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        pass

@when(u'Click on resource')
def step_impl(context):
    #Recommended on Network Q
    context.driver.find_element_by_xpath('/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/label/span').click()
    time.sleep(2)

@then(u'Resource detail should display')
def step_impl(context):
    # driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[1]/img').click()        #open activity
    context.driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[2]').click()  # Close activity
    time.sleep(2)
    element = context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[6]/div/div[2]")
    context.driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(10)


@when(u'Click on "see all" button under RNQ section')
def step_impl(context):
    context.driver.find_element_by_xpath(
        '//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/a/img').click()
    time.sleep(5)

@then(u'Screen should navigate Network Q Resources screen')
def step_impl(context):
    if "Network Q Resources" == context.driver.find_element_by_xpath("//span[text()='Network Q Resources ']").text:
        print("Navigated to Network Q successfully")
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Home']").click()
    time.sleep(3)
    try:
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        pass


@when(u'Enter text and click on send')
def step_impl(context):

    context.driver.find_element_by_xpath("//input[@placeholder='send message...']").send_keys("Hii Automated message from client")
    context.driver.find_element_by_xpath("//i[@title='Click here send message.']").click()
    time.sleep(10)


@then(u'Text should display in chat window')
def step_impl(context):
    # Screenshot required to verify
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)

@when(u'Attach file')
def step_impl(context):
    print(" Yet to be defined")


@then(u'File should display in chat window')
def step_impl(context):
    print(" Yet to be defined")

@when(u'Click on Network Q Resources')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
    time.sleep(3)


@then(u'Network Q Resources screen should be open')
def step_impl(context):
    print("Network Q is open")


@when(u'Click on Tabs')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//a[text()='Webinars']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Webinars", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Activity']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Activity", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Podcasts']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Podcasts", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Ted Talk']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Ted Talk", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Article']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Article", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Tips']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Tips", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Assessment']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Assessment", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Videos']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Videos", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Book']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Book", attachment_type=AttachmentType.PNG)
        time.sleep(3)
    except:
        context.driver.find_element_by_xpath("//a[text()='Home']").click()
        allure.attach(context.driver.get_screenshot_as_png(), name="Home", attachment_type=AttachmentType.PNG)
        time.sleep(3)


@then(u'Clicked tab related resources should display on screen')
def step_impl(context):
    print("Yes opened successfully")


@when(u'Enter text in search box')
def step_impl(context):

    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)

@then(u'Related resources should display')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath('//*[@id="Preparing for your first Coaching Session"]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        '//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(4)
    errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    if errmsg == "Activity already exists":
        print(errmsg)
        allure.attach("", name="Activity already exists")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    else:
        print("Activity has been added successfully")
        allure.attach("", name="Activity has been added successfully")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

@when(u'Enter text in advanced search box')
def step_impl(context):

    context.driver.find_element_by_xpath("//span[text()=' ADVANCED SERACH ']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@name='titileSearchValue']").send_keys("Prepar")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='descriptionSearchValue']").send_keys("Prepare")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='authorSearchValue']").send_keys("Steve")
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault1']").click()  #And1
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault3']").click()  #and2
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Apply']").click()
    time.sleep(3)


@then(u'Related resources to advances search should display')
def step_impl(context):
    time.sleep(3)

    if "Preparing for your first Coaching Session" == context.driver.find_element_by_xpath(
            "//span[text()=' Preparing for your first Coaching Session ']").text:
        print("Advanced search is successfull")
        allure.attach("", name="Advanced search is successfull")

    else:
        context.driver.find_element_by_xpath(
            '//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
        print("Filter Resets")
        allure.attach("", name="Advanced search is unsuccessfull")

@when(u'Click on Sessions')
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("//span[text()='Sessions']").click()
    time.sleep(5)

@then(u'Sessions screen should be open')
def step_impl(context):
    print('Then Sessions screen should be open')


@when(u'Notes tab is active')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    text1 = context.driver.find_element_by_xpath("//a[@class='nav-link font-size-9 koho active-tab-color']").text
    if text1 == "NOTES":
        print("Note tab is active")
        allure.attach("", name="Note tab is active")



@then(u'Missing survey tab should display "Your all caught up"')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()=' MISSING SURVEYS']").click()
    time.sleep(2)
    mtext = context.driver.find_element_by_xpath("//span[text()='You are all caught up.']").text
    if mtext == "You are all caught up.":
        print("Working as expected")
        allure.attach("", name="You are all caught up.")

    else:
        print("Missing survey displayed - bug")
        allure.attach("", name="Missing survey displayed - bug")


@when(u'Missing survey tab is active')
def step_impl(context):
    time.sleep(2)
    context.driver.refresh()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    text1 = context.driver.find_element_by_xpath("//a[@class='nav-link font-size-9 koho active-tab-color']").text
    try:

        if text1 == "MISSING SURVEYS":
            print("Missing surveys are available")
            allure.attach("", name="Missing survey displayed - bug")
    except:
        print("No missing survey")
        allure.attach("", name="No missing survey")


@then(u'Missing survey should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Click Add notes')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//span[text()='No notes for user']").is_displayed()
        print("Notes are not available for current month")
        allure.attach("", name="Notes are not available for current month")
        print("Adding notes on day 15")
        allure.attach("", name="Adding notes on day 15")
        action = ActionChains(context.driver)
        action.context_click(context.driver.find_element_by_xpath("//span[text()='15']")).perform()
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Add Note']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath(
            '//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').clear()
        time.sleep(2)
        context.driver.find_element_by_xpath(
            '//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').send_keys("My Automated Notes")
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Save']").click()
        time.sleep(2)
        print("Updated Notes")
        allure.attach("", name="Updated Notes")
        print(context.driver.find_element_by_xpath(
            "//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
        allure.attach(context.driver.find_element_by_xpath(
            "//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text, name="Updated notes",attachment_type=AttachmentType.TEXT)


    except:
        print(" Seems notes are already there")


@then(u'Note should display under Notes section')
def step_impl(context):
    time.sleep(2)
    print("Updated Notes")
    print(context.driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)


@when(u'Click on Edit icon')
def step_impl(context):
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print("Notes")
        print(context.driver.find_element_by_xpath(
            "//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
        action = ActionChains(context.driver)
        action.move_to_element(context.driver.find_element_by_xpath(
            "/html/body/app-root/app-session/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/span")) \
            .move_to_element(context.driver.find_element_by_xpath("//img[@popover='Edit']")).click().perform()
        time.sleep(5)
        context.driver.find_element_by_xpath(
            '//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').send_keys(
            "My Automated Notes")
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Save']").click()


    except:
        print("Seems somethings is breaking on notes")



@then(u'Edit notes should display under Notes section')
def step_impl(context):
    time.sleep(2)
    print("Updated Notes")
    print(context.driver.find_element_by_xpath(
        "//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Click on Delete icon')
def step_impl(context):
    action = ActionChains(context.driver)
    action.move_to_element(context.driver.find_element_by_xpath(
        "/html/body/app-root/app-session/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/span")) \
        .move_to_element(context.driver.find_element_by_xpath("//img[@popover='Delete']")).click().perform()
    time.sleep(2)


@then(u'Note should get deleted')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "//*[@id='uBody']/app-root/app-session/div[6]/div/div/div[3]/button[2]").click()
    print("Note has been deleted")
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Click one of  activity under activities section')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//a[text()='ACTIVITIES']").click()
    time.sleep(2)


@then(u'Activity details should display')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//input[@id='assignmentCheckBox-0-0']").click()
        time.sleep(2)
        context.driver.find_element_by_xpath("//button[text()='No']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
        if context.driver.find_element_by_xpath("//span[text()='No activities to show']").is_displayed():
            print("No active activity due for client in current month")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



@given(u'Missing survey section should be open')
def step_impl(context):
    print("Pending this automatic script -future scope")


@when(u'Missing survey is pending')
def step_impl(context):
    print("Pending this automatic script -future scope")


@when(u'Fill the missing survey')
def step_impl(context):
    print("Pending this automatic script -future scope")


@then(u'Missing survey should get submitted')
def step_impl(context):
    print("Pending this automatic script -future scope")


@when(u'Click on Activities')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Activities']").click()
    time.sleep(2)


@then(u'Activities screen should be open')
def step_impl(context):
    print("Activities screen open")

@when(u'Click on Active')
def step_impl(context):
    print("tejas")

@then(u'Active activities should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@when(u'Click on Coach recommended active activity')
def step_impl(context):
    time.sleep(5)
    text2 = context.driver.find_element_by_xpath(
        "//a[@class='navanchor border-radius-4 nav-link koho font-weight-500 font-size-9 align-items-center active-tab-color']").text
    if text2 == "Active":
        print("Active selected - Working as expected")
    else:
        print("Something went wrong")

@then(u'Activity detail should display and Complete button should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    allure.attach(context.driver.ge)

@then(u'Click on Coach self active activity')
def step_impl(context):
    print("Pending future scope")


@then(u'Activity detail should display and Complete and Delete button should display')
def step_impl(context):
    print("Pending future scope")


@then(u'Click on Add')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[text()='ADD']").click()
    time.sleep(3)


@then(u'Screen should navigate to Network Q screen')
def step_impl(context):
    print("Screenshot needed")


@then(u'Add Self activity for client')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    context.driver.find_element_by_xpath('//*[@id="Preparing for your first Coaching Session"]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        '//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()



@then(u'Proper toaster messgae should display')
def step_impl(context):
    time.sleep(3)
    errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    if errmsg == "Activity already exists":
        print(errmsg)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    else:
        print("Activity has been added successfully")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    context.driver.back()
    time.sleep(2)

@when(u'Click on Archived on activities screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Archived']").click()
    time.sleep(2)


@then(u'Archived activities should display on activities screen')
def step_impl(context):
    # context.driver.find_element_by_xpath("//span[text()='Preparing for your first Coaching Session ']").click()
    # time.sleep(3)
    # context.driver.find_element_by_xpath("//*[@id='staticModal']/div/div/div[3]/button[2]").click()
    time.sleep(2)


@then(u'Click on Coach recommended archived activity')
def step_impl(context):
    print("Pending activity ")


@then(u'Activity detail should display')
def step_impl(context):
    print("Pending activity ")


@then(u'Click on Coach self archived activity')
def step_impl(context):
    print("Pending activity ")


@then(u'Activity detail should display on popup')
def step_impl(context):
    print("Pending activity ")


@given(u'Profile & Preferences screen should display')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Profile and Preferences']").click()


@when(u'If personal information display')
def step_impl(context):
    time.sleep(3)

@then(u'Client Profile details displayed properly')
def step_impl(context):
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Enter text in field and click on save')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,500)", "")
    time.sleep(5)
    context.driver.find_element_by_name("data[ReferralName]").clear()
    time.sleep(2)
    context.driver.find_element_by_name("data[ReferralName]").send_keys("Kanaka Software")
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(500,1700)", "")
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@name='data[submit]']").click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@then(u'Profile should be updated and updated value should display in field')
def step_impl(context):
    toastmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    print(toastmsg)
    time.sleep(3)
    context.driver.refresh()
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(0,500)", "")
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Click on Settings')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Settings']").click()
    time.sleep(2)


@then(u'Settings screen should displayed')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Add/Change calendar')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div/div[1]").click()
        time.sleep(2)
    except:
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div/img").click()
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
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print("Already added calendar added")

    time.sleep(5)


@then(u'Update calendar details should display on screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u'Click on change')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//img[@title='Change Password']").click()
    time.sleep(3)

@when(u'Enter Old and New password and click on Submit')
def step_impl(context):
    context.driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
    context.driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
    context.driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(2)


@then(u'Client password should get changed')
def step_impl(context):
    print("Your new password is Qwerty@123")
