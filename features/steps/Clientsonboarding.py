import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb


@given(u': Temporary mail should be opened')
def step_impl(context):
    context.driver.execute_script("window.open('about:blank','tempmail');")
    context.driver.switch_to.window("tempmail")
    context.driver.get(gb.TEMPURL)
    # context.driver.maximize_window()

    time.sleep(15)
    context.driver.find_element_by_id("click-to-delete").click()
    time.sleep(15)
    context.driver.find_element_by_id('click-to-copy').click()


@when(u': Send an invitation to individual client')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    time.sleep(5)
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
    context.driver.find_element_by_name("individualclientfirstname").send_keys("IndividualAutomate")
    context.driver.find_element_by_name("individualclientlastname").send_keys("Client")
    context.driver.find_element_by_name("individualclientemail").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("individualclientallocationhour").send_keys("55")
    time.sleep(5)
    context.driver.find_element_by_id("btndisable").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)


@when(u': Complete the onboarding process')
def step_impl(context):
    context.driver.switch_to.window("tempmail")
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)

    context.driver.find_element_by_link_text("Welcome to Quantuvos!").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(5)
    context.driver.find_element_by_link_text("Start").click()
    time.sleep(10)

    time.sleep(10)
    context.driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

    context.driver.execute_script("window.open('about:blank','thirdtab');")
    context.driver.switch_to.window("thirdtab")
    context.driver.get(gb.TEMPURL)
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_link_text("Please confirm your email").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 600)")
    context.driver.find_element_by_link_text("Confirm").click()
    time.sleep(10)

    context.driver.find_element_by_id("password").send_keys(gb.password)
    context.driver.find_element_by_id("confirmPassword").send_keys(gb.password)

    time.sleep(3)
    context.driver.find_element_by_id("btnNext").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

    time.sleep(5)
    context.driver.find_element_by_xpath("//span[text()='Login ']").click()
    time.sleep(5)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)

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


@when(u': Schedule the first session')
def step_impl(context):
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

    context.driver.execute_script("window.open('about:blank','forthtab');")
    context.driver.switch_to.window("forthtab")
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)

    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[2]/div[3]/div/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[3]/button/span").click()
    time.sleep(5)


    try:
        context.driver.find_element_by_id("07:00 AM").click()
        time.sleep(2)
    except Exception:
        print("7 am coach busy")

    try:
        context.driver.find_element_by_id("08:00 AM").click()
        time.sleep(2)
    except Exception:
        print("8 am coach busy")

    try:
        context.driver.find_element_by_id("09:00 AM").click()
        time.sleep(2)
    except Exception:
        print("9 am coach busy")

    try:
        context.driver.find_element_by_id("10:00 AM").click()
        time.sleep(2)
    except Exception:
        print("10 am coach busy")

    try:
        context.driver.find_element_by_id("11:00 AM").click()
        time.sleep(2)
    except Exception:
        print("11 am coach busy")

    try:
        context.driver.find_element_by_id("12:00 PM").click()
        time.sleep(2)
    except Exception:
        print("12 am coach busy")

    try:
        context.driver.find_element_by_id("01:00 PM").click()
        time.sleep(2)
    except Exception:
        print("01 pm coach busy")

    try:
        context.driver.find_element_by_id("02:00 PM").click()
        time.sleep(2)
    except Exception:
        print("02 pm coach busy")

    try:
        context.driver.find_element_by_id("03:00 PM").click()
        time.sleep(2)
    except Exception:
        print("03 pm coach busy")

    try:
        context.driver.find_element_by_id("04:00 PM").click()
        time.sleep(2)
    except Exception:
        print("04 pm coach busy")

    try:
        context.driver.find_element_by_id("05:00 PM").click()
        time.sleep(2)
    except Exception:
        print("05 pm coach busy")

    try:
        context.driver.find_element_by_id("06:00 PM").click()
        time.sleep(2)
    except Exception:
        print("06 pm coach busy")

    try:
        context.driver.find_element_by_id("07:00 PM").click()
        time.sleep(2)
    except Exception:
        print("07 pm coach busy")

    try:
        context.driver.find_element_by_id("08:00 PM").click()
        time.sleep(2)
    except Exception:
        print("08 pm coach busy")

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


@when(u': Send an invitation to customer client')
def step_impl(context):
    context.driver.switch_to.window("opsdashboard")
    time.sleep(10)
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("clienttype").click()

    time.sleep(10)
    context.driver.find_element_by_name("customerclientfirstname").send_keys("CustomerAutomate")
    context.driver.find_element_by_name("customerclientlastname").send_keys("Client")
    context.driver.find_element_by_name("customerclientemail").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("customerclientallocationhour").send_keys("65")
    context.driver.find_element_by_name("customerclientcompanyid").send_keys("5")
    time.sleep(5)
    context.driver.find_element_by_id("btnsubmit").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)
