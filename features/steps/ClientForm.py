import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from allure_behave.hooks import allure_report


@given('Launch the Chrome browser')
def lauchbrowser(context):
    context.driver = webdriver.Chrome()


@when(u'Open login page')
def step_impl(context):
    context.driver.get("https://platform-dev.quantuvos.com/login")
    context.driver.maximize_window()


@when(u'Enter login email "{email}" and password "{password}"')
def entercredentials(context, email, password):
    context.driver.find_element_by_id("inputEmailID").send_keys(email)
    context.driver.find_element_by_id("inputPasswordID").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()


@when(u'Enter the details')
def step_impl(context):
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
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    time.sleep(5)
    context.driver.find_element_by_name("data[CurrentRole]").send_keys("Manager")
    # context.driver.find_element_by_name("data[CoachingSessionTime][weekday]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    # Coaching Preferences information optional
    context.driver.implicitly_wait(10)
    context.driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath("/html/body/app-root/app-clientform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[2]/label").click()
    context.driver.find_element_by_name("data[SessionTitle]").send_keys("First Automation")
    context.driver.find_element_by_name("data[TopicDetails]").send_keys("First automation topic")
    context.driver.execute_script("window.scrollTo(0, 200)")
    context.driver.find_element_by_name("data[Agreement]").click()
    time.sleep(10)


@when(u'Click on Submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Click on Ok')
    #context.driver.find_element_by_xpath('//*[@id="ewdsgoh"]').click()


@then(u'Click on Ok')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Click on Ok')

#allure_report(r"C:\Users\kanaka\PycharmProjects\Qworkspace")