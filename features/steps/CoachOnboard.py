from behave import *
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
import time
from features import myglobal as gb

@given(u'Laumch the browser')
def step_impl(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)


@given(u'open the Hit the temp URL')
def step_impl(context):
    context.driver.get(gb.TEMPURL)
    context.driver.maximize_window()


@given(u'Copy the temp email address')
def step_impl(context):
    time.sleep(15)
    context.driver.find_element_by_id('click-to-copy').click()


@given(u'Login as operation user')
def step_impl(context):
    context.driver.execute_script("window.open('about:blank','opslogin');")
    context.driver.switch_to.window("opslogin")
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    time.sleep(10)


    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(gb.opsemail)
    context.driver.find_element_by_name("password").send_keys(gb.opspassword)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@given(u'Send Invitation to coach')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(3)
    context.driver.find_element_by_id("coachtype").click()
    time.sleep(5)
    context.driver.find_element_by_name("coachfirstname").send_keys("CoachABC")
    context.driver.find_element_by_name("coachlastname").send_keys("XYZ")
    context.driver.find_element_by_name("coachemail").send_keys(Keys.CONTROL, 'v')
    time.sleep(5)
    context.driver.find_element_by_id("coachbtn").click()
    time.sleep(5)


@given(u'Again go to temp')
def step_impl(context):
    context.driver.switch_to.window(context.driver.window_handles[0])
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)


@given(u'select mail and Click on Start')
def step_impl(context):
    context.driver.find_element_by_link_text("quantuvos@gmail.com").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(5)
    context.driver.find_element_by_link_text("Start").click()
    time.sleep(10)


@given(u'Confirm the email address')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)


@given(u'Once again go to temp')
def step_impl(context):
    context.driver.execute_script("window.open('about:blank','tempmail');")
    context.driver.switch_to.window("tempmail")
    context.driver.get(gb.TEMPURL)
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)


@given(u'Select mail and click on confirm')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_link_text("Quantuvos Coach Email Confirmation").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 700)")
    context.driver.find_element_by_link_text("Confirm").click()
    time.sleep(10)


@given(u'Set the password')
def step_impl(context):
    context.driver.find_element_by_id("password").send_keys(gb.password)
    context.driver.find_element_by_id("confirmPassword").send_keys(gb.password)
    time.sleep(3)
    context.driver.find_element_by_id("btnNext").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)



@given(u'login as coach user')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)


@given(u'Fill the coach detail')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[2]/button").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//div[@data-value='Albania']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Self']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/input").send_keys("Automation")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(3)
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys("1234567890")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]").click()
    context.driver.find_element_by_xpath("//div[@data-value='Female']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]").click()
    context.driver.find_element_by_xpath("//div[@data-value='25-35']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//div[@data-value='Married']").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[5]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[6]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[8]/div[1]/div[2]/label/input").click()
    context.driver.execute_script("window.scrollTo(500, document.body.scrollHeight)")
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[7]/div[1]/input").send_keys("Master in Automation")
    time.sleep(3)

@then(u'Coach profile submitted')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coach-calendar-access/div[1]/div[3]/button/span").click()
    time.sleep(5)

