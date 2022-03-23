import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb, environment


@given(u': Client should login into system with "{email}" and "{password}" credentials')
def step_impl(context,email,password):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)



@when(u': Check Next session is scheduled or not')
def step_impl(context):

    try:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        print("No survey pending")

    ##Next Session
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    if context.driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").is_enabled():
        print("Join session button is disabled")
    else:
        context.driver.find_element_by_xpath("//span[text()=' JOIN SESSION ']").click()
        print("Session details showed")


@when(u': Check Coaching Goals functionality')
def step_impl(context):
    #Coaching Goals
    time.sleep(5)
    try:
        context.driver.find_element_by_xpath("//span[text()=' ADD']").click()
        print("Creating new goal")
    except:
        print("Goals already set")
        context.driver.find_element_by_xpath("//span[text()='EDIT']").click()

    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.CONTROL,'a')
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(Keys.DELETE)
    time.sleep(5)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys("My Goals")
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()

    text1 = context.driver.find_element_by_xpath('//*[@id="coachingGoals-Parent"]/div/div[2]/ul/li/p').text
    if text1 == "My Goals":
        print("Coaching Goals set successfully")

    else:
        print(" Not able to set coaching goals")

    #Scenario2
    context.driver.find_element_by_xpath("//span[text()='EDIT']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.CONTROL, 'a')
    context.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[2]/ckeditor/div[2]/div[2]/div").send_keys(
        Keys.DELETE)
    time.sleep(3)
    context.driver.find_element_by_xpath("//*[@id='richtextId']/button[1]").click()
    time.sleep(2)
    text1 = context.driver.find_element_by_xpath("//span[text()=' ADD']").text
    if text1 == "ADD":
        print("Goals has been deleted successfully")

    else:
        print("Something went wrong goals not deleted")


@when(u': Check activities section')
def step_impl(context):
    #Activities
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='ACTIVE']").click()
    time.sleep(5)
    try:
        element = context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only self activities are here")

    except:
        element = context.driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only coach activities are here")
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='ARCHIVED']").click()
    time.sleep(5)
    try:
        element = context.driver.find_element_by_xpath(
            '/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[3]')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only self activities are here")

    except:
        element = context.driver.find_element_by_xpath(' //*[@id="assignmentsRow"]/div[3]/button/span')
        context.driver.execute_script("return arguments[0].scrollIntoView();", element)
        # print("Only coach activities are here")

    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/a/img').click()
    time.sleep(5)
    if " Activities" == context.driver.find_element_by_xpath("//span[text()=' Activities']").text:
        print("Naviagated to Activities page successfully")

    context.driver.find_element_by_xpath("//span[text()='Home']").click()
    time.sleep(3)
    try:
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        print("No survey popup display")


@when(u': Check recommeneded on network q functionality')
def step_impl(context):


    #Recommended on Network Q
    context.driver.find_element_by_xpath('/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/label/span').click()
    time.sleep(2)
    #driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[1]/img').click()        #open activity
    context.driver.find_element_by_xpath('//*[@id="staticModal"]/div/div/div[3]/button[2]').click()     # Close activity
    time.sleep(2)
    element = context.driver.find_element_by_xpath("/html/body/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[6]/div/div[2]")
    context.driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(10)
    context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/a/img').click()
    time.sleep(5)
    if "Network Q Resources" == context.driver.find_element_by_xpath("//span[text()='Network Q Resources ']").text:
        print("Navigated to Network Q successfully")
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Home']").click()
    time.sleep(3)
    try:
        context.driver.find_element_by_xpath('//*[@id="postSurveyPOPUP"]/div/div/div[1]/span/img').click()
        time.sleep(3)
    except:
        print("No survey popup display")


@when(u': Check Chat Functionality')
def step_impl(context):


    context.driver.find_element_by_xpath("//input[@placeholder='send message...']").send_keys("Hii Automated message from client")
    context.driver.find_element_by_xpath("//i[@title='Click here send message.']").click()
    time.sleep(10)
    #Screenshot required to verify
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)

    #sendfilenotworking
    #uploadfile = context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-client-dashboard/div[1]/div/div[2]/div/div[2]/div[2]/app-chat/div/div/div[3]/button[2]/i')
    #uploadfile.send_keys("C://Users//kanaka//Downloads//+firstclients.csv")


@then(u': Client dashboard- Home screen should work as expected')
def step_impl(context):
    print("dashboard functionality working as expected")


@given(u': Network Q screen should be open')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='Network Q Resources']").click()
    time.sleep(3)

@when(u': Check all tabs on network q screen')
def step_impl(context):

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
    time.sleep(3)

@when(u': Check Search functionality')
def step_impl(context):

    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath('//*[@id="Preparing for your first Coaching Session"]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(4)
    errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    if errmsg == "Activity already exists":
        print(errmsg)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    else:
        print("Activity has been added successfully")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

@when(u': Check Advanced search Functionality')
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

    if "Preparing for your first Coaching Session" == context.driver.find_element_by_xpath("//span[text()=' Preparing for your first Coaching Session ']").text:
        print("Advanced search is successfull")
    else:
        context.driver.find_element_by_xpath('//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
        print("Filter Resets")


@then(u': Network  Q screen should work as expected')
def step_impl(context):
    print("working as expected Network Q")


@given(u': Session screen should be open')
def step_impl(context):

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("//span[text()='Sessions']").click()
    time.sleep(5)

@when(u': Check Notes section in session screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    text1 = context.driver.find_element_by_xpath("//a[@class='nav-link font-size-9 koho active-tab-color']").text
    if text1 == "NOTES":
        print("No Missing survey")
    elif text1 == "ACTIVITIES":
        print("Error occurred activities default selected")
    else:
        print("Missing survey are pending")
        context.driver.find_element_by_xpath("//a[text()='NOTES']").click()

    try:
        context.driver.find_element_by_xpath("//span[text()='No notes for user']").is_displayed()
        print("Notes are not available for current month")
        print("Adding notes on day 15")
        action = ActionChains(context.driver)
        action.context_click(context.driver.find_element_by_xpath("//span[text()='15']")).perform()
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Add Note']").click()
        time.sleep(3)
        context.driver.find_element_by_xpath('//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').send_keys(
            "My Automated Notes")
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Save']").click()
        time.sleep(2)
        print("Updated Notes")
        print(context.driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)


    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        print("Notes")
        print(context.driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
        action = ActionChains(context.driver)
        action.move_to_element(context.driver.find_element_by_xpath(
            "/html/body/app-root/app-session/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/span")) \
            .move_to_element(context.driver.find_element_by_xpath("//img[@popover='Edit']")).click().perform()
        time.sleep(5)
        context.driver.find_element_by_xpath('//*[@id="AddNoteModel"]/div/div/div[2]/ckeditor/div[2]/div[2]/div').send_keys(
            "My Automated Notes")
        time.sleep(2)
        context.driver.find_element_by_xpath("//span[text()='Save']").click()
        time.sleep(2)
        print("Updated Notes")
        print(context.driver.find_element_by_xpath("//div[@class='noteParentContainer w-70 pointer ng-star-inserted']").text)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    # deleting the created activity
    action = ActionChains(context.driver)
    action.move_to_element(context.driver.find_element_by_xpath(
        "/html/body/app-root/app-session/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/span")) \
        .move_to_element(context.driver.find_element_by_xpath("//img[@popover='Delete']")).click().perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='uBody']/app-root/app-session/div[6]/div/div/div[3]/button[2]").click()
    print("Note has been deleted")
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u': Check Activities section on session screen')
def step_impl(context):

    time.sleep(5)
    context.driver.find_element_by_xpath("//a[text()='ACTIVITIES']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//input[@id='assignmentCheckBox-0-0']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='No']").click()
    time.sleep(3)


@when(u': Check missing survey section on session screen')
def step_impl(context):
    print("Pending this automatic script -future scope")


@when(u': Check session scheduling functionality')
def step_impl(context):
    print("Soon will add code here")


@then(u': Sessions screen should work as expected')
def step_impl(context):
    print("Working as expected")


@given(u': Activities screen should be open')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Activities']").click()

@when(u': Check active activities section')
def step_impl(context):
    time.sleep(5)
    text2 = context.driver.find_element_by_xpath(
        "//a[@class='navanchor border-radius-4 nav-link koho font-weight-500 font-size-9 align-items-center active-tab-color']").text
    if text2 == "Active":
        print("Working as expected")
    else:
        print("Something went wrong")


@when(u': Check Add self activity functionality')
def step_impl(context):

    context.driver.find_element_by_xpath("//a[text()='ADD']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="run"]/h6').click()
    time.sleep(3)
    context.driver.find_element_by_xpath('//*[@id="Preparing for your first Coaching Session"]').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="uBody"]/app-root/app-network-q-resources/div[2]/div/div/div[3]/button[2]').click()
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


@when(u': Check archived activities section')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Archived']").click()
    time.sleep(2)
    # context.driver.find_element_by_xpath("//span[text()='Preparing for your first Coaching Session ']").click()
    # time.sleep(3)
    # context.driver.find_element_by_xpath("//*[@id='staticModal']/div/div/div[3]/button[2]").click()
    # time.sleep(2)

@then(u': Activities screen should work as expected')
def step_impl(context):
    print('Activities screen should work as expected')


@given(u': Profile & Preferences screen should be open')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Profile and Preferences']").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


@when(u': Check update preference functionality')
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,700)", "")
    time.sleep(5)
    context.driver.find_element_by_name("data[ReferralName]").send_keys("Kanaka Software")
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(800,1700)", "")
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@name='data[submit]']").click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@then(u': Preferences should updated successfully')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Activities']").click()
    context.driver.find_element_by_xpath("//span[text()=' Profile and Preferences']").click()
    time.sleep(3)
    context.driver.execute_script("window.scrollBy(0,800)", "")
    time.sleep(5)
    print(context.driver.find_element_by_name("data[ReferralName]").text)
    if context.driver.find_element_by_name("data[ReferralName]").text == "Kanaka Software":
        print("Profile & preferences updated successfully")
    else:
        print("Something went wrong in PP")


@given(u': Settings screen should be open')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Settings']").click()
    time.sleep(2)

@when(u': Check Add/Change calendar functionality')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div[1]/div/div[1]").click()
        time.sleep(2)
    except:
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-setting/div[1]/div/div[2]/div/div/div/div/div/form/div[2]/div/div/img").click()
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
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)
    context.driver.find_element_by_xpath('//*[@id="idBtn_Accept"]').click()
    time.sleep(2)


@when(u': Check Change password functionality')
def step_impl(context):

    context.driver.find_element_by_xpath("//img[@title='Change Password']").click()
    time.sleep(3)
    context.driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
    context.driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
    context.driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(2)


@then(u': Both test cases should pass')
def step_impl(context):
    print("Your new password is Qwerty@123")

