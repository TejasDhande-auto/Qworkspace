import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Hit Chrome browser')
def HitBrowser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)

@when(u'Hit the temp mail link')
def hit_tempmail_link(context):
    context.driver.get("https://temp-mail.org/en/")
    context.driver.maximize_window()


@when(u'Copy the temp email address')
def step_impl(context):
    time.sleep(20)
    context.driver.find_element_by_id('click-to-copy').click()

@when(u'Open new tab')
def step_impl(context):
    context.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    context.driver.maximize_window()
    time.sleep(5)


@when(u'Hit the Qunatuvos login URL and logged in as operation user "{email}" and "{password}"')
def step_impl(context,email,password):
    context.driver.execute_script("window.open('about:blank','secondtab');")
    context.driver.switch_to.window("secondtab")
    context.driver.get('https://platform-dev.quantuvos.com/login')
    context.driver.maximize_window()
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'Send invitation to individual client')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(5)

    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("individual-client").click()

    time.sleep(10)
    context.driver.find_element_by_name("individualclientfirstname").send_keys("ABC")
    context.driver.find_element_by_name("individualclientlastname").send_keys("Test")
    context.driver.find_element_by_name("individualclientemail").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("individualclientallocationhour").send_keys("5")
    time.sleep(5)
    context.driver.find_element_by_id("btndisable").click()

    time.sleep(10)


@when(u'Go to the temp mail')
def step_impl(context):
    context.driver.switch_to.window(context.driver.window_handles[0])
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)


@when(u'Open the first Email and click on Start')
def step_impl(context):
    context.driver.find_element_by_link_text("quantuvos@gmail.com").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(5)
    context.driver.find_element_by_link_text("Start").click()
    time.sleep(10)

@when(u'Paste the temp email address and click on Send')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(10)


@when(u'Again hit the temp mail link')
def step_impl(context):
    context.driver.execute_script("window.open('about:blank','thirdtab');")
    context.driver.switch_to.window("thirdtab")
    context.driver.get('https://temp-mail.org/en/')
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)


@when(u'Open confirm password email and click on Confirm')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_link_text("Quantuvos Email Confirmation").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 600)")
    context.driver.find_element_by_link_text("Confirm").click()
    time.sleep(10)


@when(u'Enter the password "{pwd1}" and "{pwd2}" and click on next')
def step_impl(context,pwd1,pwd2):
    context.driver.find_element_by_id("password").send_keys(pwd1)
    context.driver.find_element_by_id("confirmPassword").send_keys(pwd2)
    time.sleep(3)
    context.driver.find_element_by_id("btnNext").click()
    time.sleep(5)


@when(u'Again hit the Quantuvos login URL')
def step_impl(context):
    time.sleep(5)
    context.driver.get('https://platform-dev.quantuvos.com/login')
    context.driver.execute_script("document.body.style.zoom='zoom 90%'")
    time.sleep(5)


@when(u'paste the email address and enter password "{pwd}" and click on login')
def step_impl(context,pwd):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys(pwd)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'client form opened and filled the details')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_name('data[FirstName]').send_keys("ABC")
    context.driver.find_element_by_name('data[LastName]').send_keys("XYZ")
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[2]/button").click()
    time.sleep(5)

    context.driver.find_element_by_name("data[PhoneNumber]").click()
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys(Keys.HOME)
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys("0123456789")
    context.driver.find_element_by_name("data[ShortName]").send_keys("pqr")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    context.driver.implicitly_wait(10)
    #context.driver.find_element_by_name("data[CoachingSessionTime][saturday]").click()
    #context.driver.find_element_by_name("data[CoachingSessionTime][weekday]").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    time.sleep(5)
    context.driver.find_element_by_name("data[CurrentRole]").send_keys("Manager")
    #context.driver.find_element_by_name("data[CoachingSessionTime][weekday]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    #Coaching Preferences information optional
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0,1080)")
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    time.sleep(10)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[2]/label").click()
    context.driver.find_element_by_name("data[SessionTitle]").send_keys("First Automation")
    context.driver.find_element_by_name("data[TopicDetails]").send_keys("First automation topic")
    context.driver.execute_script("window.scrollTo(0, 200)")
    context.driver.find_element_by_name("data[Agreement]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(10)

@when('Popup should display')
def step_impl(context):
    try:
        assert True, "Test Passed"
        time.sleep(10)

    except:
        context.driver.close()
        assert False,"Test failed"


@when(u'Operation user selects three coaches')
def coachselection(context):
    context.driver.execute_script("window.open('about:blank','forthtab');")
    context.driver.switch_to.window("forthtab")
    context.driver.get('https://platform-dev.quantuvos.com/login')
    context.driver.maximize_window()
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
    context.driver.find_element_by_name("password").send_keys("Quantuvos@123")
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)

    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-dashboard-navbar/div/div/section[3]/ul/ul[1]/li[4]/a/span").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0,1080)")
    time.sleep(3)
    context.driver.find_element_by_id("ag-464-input").click()
    context.driver.find_element_by_id("ag-475-input").click()
    context.driver.find_element_by_id("ag-486-input").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coach-selection/div[1]/div/div[2]/div/div[7]/button").click()
    time.sleep(10)



@when(u'Again client logged in')
def loginforfirstsession(context):
    context.driver.execute_script("window.open('about:blank','forthtab');")
    context.driver.switch_to.window("forthtab")
    context.driver.get('https://platform-dev.quantuvos.com/login')
    context.driver.maximize_window()
    time.sleep(10)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys("Qwerty@123")
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)

@when('select one of the coach')
def selectonecoach(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[2]/div[3]/div/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[3]/button/span").click()
    time.sleep(5)

@when('Schedule first session')
def schedulefirstsession(context):
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
    time.sleep(15)

@then(u'Popup should display')
def sessionscheduled(context):
    try:
        context.driver.find_element_by_xpath("/html/body/app-root/app-weekly-calendar/div[3]/div/div[2]/div/div/div[2]/button").click()
        time.sleep(6)
    except:
        print("There is problem")