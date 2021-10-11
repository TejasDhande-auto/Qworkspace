import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver

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
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("individual-client").click()

    time.sleep(10)
    context.driver.find_element_by_name("individualclientfirstname").send_keys("Qa")
    context.driver.find_element_by_name("individualclientlastname").send_keys("Test")
    context.driver.find_element_by_name("individualclientemail").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("individualclientallocationhour").send_keys("5")

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
    time.sleep(5)


@when(u'paste the email address and enter password "{pwd}" and click on login')
def step_impl(context,pwd):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("password").send_keys(pwd)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@then(u'client is opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then client is opened')
