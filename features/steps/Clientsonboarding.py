import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb,environment as env

@when(u': Send an invitation to individual client (name="{name}",email="{email}",hours="{hours}")')
def step_impl(context,name,email,hours):
    context.driver.execute_script("window.open('about:blank','opsdashboard');")
    context.driver.switch_to.window("opsdashboard")
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(gb.opsemail)
    context.driver.find_element_by_name("password").send_keys(gb.opspassword)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)

    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(5)

    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("individual-client").click()

    time.sleep(10)
    context.driver.find_element_by_name("individualclientfirstname").send_keys(name)
    context.driver.find_element_by_name("individualclientlastname").send_keys("Plusclient")
    context.driver.find_element_by_name("individualclientemail").send_keys(email)
    context.driver.find_element_by_name("individualclientallocationhour").send_keys(hours)
    time.sleep(5)
    context.driver.find_element_by_id("btndisable").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)


@when(u': Complete the onboarding process (email="{email}")')
def step_impl(context,email):
    try:
        context.driver.switch_to.window("Mail")

    except:
        context.driver.execute_script("window.open('about:blank','Mail');")
        context.driver.switch_to.window("Mail")
        context.driver.get("https://outlook.live.com/mail")
        time.sleep(10)
        context.driver.find_element_by_link_text("Sign in").click()
        time.sleep(5)

        context.driver.find_element_by_id('i0116').send_keys("qtestclient@outlook.com")
        time.sleep(5)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(10)
        context.driver.find_element_by_xpath('//input[@type="password"]').send_keys("Kanaka@123")
        time.sleep(3)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(5)
        context.driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(10)
        try:
            context.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]").click()
            time.sleep(2)
        except:
            pass

    # First mail
    time.sleep(10)
    context.driver.find_element_by_xpath("(//span[text()='Welcome to Quantuvos!'])[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Start']").click()
    context.driver.switch_to.window(context.driver.window_handles[3])
    time.sleep(3)
    context.driver.find_element_by_xpath('//input[@id="email"]').send_keys(email)
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

    context.driver.close()

    context.driver.switch_to.window("Mail")
    time.sleep(3)
    context.driver.find_element_by_xpath("(//span[text()='Please confirm your email'])[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Confirm']").click()
    context.driver.switch_to.window(context.driver.window_handles[3])

    time.sleep(3)
    context.driver.find_element_by_xpath('//input[@name="password"]').send_keys(gb.password)
    context.driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(gb.password)

    time.sleep(5)
    context.driver.find_element_by_id("btnNext").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='Login ']").click()
    context.driver.implicitly_wait(10)

    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)

    context.driver.find_element_by_name('data[FirstName]').send_keys("ABC")
    context.driver.find_element_by_name('data[LastName]').send_keys("XYZ")
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[2]/button").click()
    time.sleep(5)

    context.driver.find_element_by_name("data[PhoneNumber]").click()
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys(Keys.HOME)
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys("0123456789")
    context.driver.find_element_by_name("data[ShortName]").send_keys("pqr")
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    context.driver.implicitly_wait(10)
    # context.driver.find_element_by_name("data[CoachingSessionTime][saturday]").click()
    # context.driver.find_element_by_name("data[CoachingSessionTime][weekday]").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(5)
    context.driver.find_element_by_xpath('(//input[@value="Select All"])[1]').click()
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    time.sleep(5)
    context.driver.find_element_by_name("data[CurrentRole]").send_keys("Manager")
    # context.driver.find_element_by_name("data[CoachingSessionTime][weekday]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    # Coaching Preferences information optional
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0,1080)")
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    time.sleep(10)
    context.driver.find_element_by_xpath("//span[text()='Career Direction/Advancement: I want to talk about what next for me or something related to advancing in my career']").click()
    #context.driver.find_element_by_name("data[SessionTitle]").send_keys("First Automation")
    #context.driver.find_element_by_name("data[TopicDetails]").send_keys("First automation topic")
    context.driver.execute_script("window.scrollTo(0, 200)")
    #context.driver.find_element_by_name("data[Agreement]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    context.driver.find_element_by_xpath("//button[text()='OK']").click()
    time.sleep(2)
    # context.driver.find_element_by_xpath("//span[text()=' Skip and Continue ']").click()
    # time.sleep(2)
    # allure.attach(context.driver.get_screenshot_as_png(), name="Info Popup", attachment_type=AttachmentType.PNG)
    # time.sleep(2)
    # context.driver.find_element_by_xpath("//button[text()='OK']").click()
    # time.sleep(2)
    # context.driver.close()

@when(u': Sync the Google Calendar')
def step_impl(context):
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
            context.driver.find_element_by_xpath("//span[text()='Continue']").click()   #driver.find_element_by_xpath("//span[text()='Cancel']").click()
            time.sleep(5)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        except:
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("",name="Access permission has already been given for selected Google calendar")

    except:
        raise Exception("Unable to sync calendar")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    time.sleep(2)
    context.driver.close()


@when(u': Schedule the first session (email="{email}")')
def step_impl(context,email):
    context.driver.switch_to.window("opsdashboard")
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-dashboard-navbar/div/div/section[3]/ul/ul[1]/li[4]/a/span").click()
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0,1080)")
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[5]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/input").click()
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[5]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/input").click()
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[5]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[3]/div[1]/div/div/div/div[2]/input").click()
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[7]/button").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

    context.driver.switch_to.window("Mail")
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='We’ve got your coaches!']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Select Your Coach']").click()
    context.driver.implicitly_wait(10)
    context.driver.switch_to.window(context.driver.window_handles[3])
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name="Calendar error", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath("//button[text()=' OK ']").click()
        allure.attach("",name="Client calendar is not properly synchronized")
    except:
        pass
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[2]/div[3]/div/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[3]/button/span").click()
    time.sleep(5)
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name="Calendar error", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath("//button[text()='Continue']").click()
        allure.attach("",name="Client calendar is not properly synchronized")
    except:
        pass
    time.sleep(5)
    env.selecttimeslotforfirstsession(context)

    context.driver.find_element_by_xpath("/html/body/app-root/app-weekly-calendar/div[3]/div/div[1]/form/div[3]/button/span").click()
    time.sleep(25)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)


@then(u': Client dashboard should be open')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("/html/body/app-root/app-weekly-calendar/div[3]/div/div[2]/div/div/div[2]/button").click()
        time.sleep(6)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        time.sleep(5)
    except:
        print("There is problem")

    context.driver.close()


@when(u': Send an invitation to customer client (name="{name}",email="{email}",hours="{hours}")')
def step_impl(context,name,email,hours):
    context.driver.switch_to.window("opsdashboard")
    time.sleep(10)
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("clienttype").click()

    time.sleep(10)
    context.driver.find_element_by_name("customerclientfirstname").send_keys(name)
    context.driver.find_element_by_name("customerclientlastname").send_keys("Plussystem")
    context.driver.find_element_by_name("customerclientemail").send_keys(email)
    context.driver.find_element_by_name("customerclientallocationhour").send_keys(hours)
    context.driver.find_element_by_name("customerclientcompanyid").send_keys("kanaka")
    time.sleep(5)
    context.driver.find_element_by_id("btnsubmit").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)

@when(u': Sync the MS calendar')
def step_impl(context):
    try:
        time.sleep(2)
        context.driver.find_element_by_xpath("//div[text()=' Microsoft calendar ']").click()
        time.sleep(3)
        context.driver.find_element_by_id('i0116').send_keys("qtestclient@outlook.com")
        time.sleep(5)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(5)
        context.driver.find_element_by_id('i0118').send_keys("Kanaka@123")
        time.sleep(3)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(3)
        try:
            context.driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
            time.sleep(3)
        except:
            pass
        try:
            context.driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(3)
            context.driver.find_element_by_xpath('//*[@id="idBtn_Accept"]').click()
            time.sleep(5)
            print("New calendar added")
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="New calendar added")

        except:
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            print("Already added calendar added")
            allure.attach("", name="Access permission has already been given for selected MS calendar")

    except:
        raise Exception("Unable to sync MS calendar")


    time.sleep(2)
    context.driver.close()