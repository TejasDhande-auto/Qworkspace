import time

import allure
from behave import *
from selenium.webdriver import ActionChains

from features import environment
from datetime import date, timedelta


@given(u'Client should logged in with valid credential "{email}" , "{password}"')
def step_impl(context,email,password):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'Schedule first session of client')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_link_text("Sessions").click()
    time.sleep(10)
    today = date.today()
    day = str(today.day + 1)
    gmailtimeslot = "07.00 AM"
    checkevent = "//span[text()='" + day + "']"
    rightclick = context.driver.find_element_by_xpath(checkevent)
    actionChains = ActionChains(context.driver)
    actionChains.context_click(rightclick).perform()

    time.sleep(10)

    context.driver.find_element_by_xpath("/html/body/div[2]/div/div/context-menu-content/div/ul/li[2]/a/h5/span").click()
    time.sleep(10)
    for i in range (1,8):
        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        selectaday = "//span[text()='" + month + " " + day + "']"
        time.sleep(2)
        context.driver.find_element_by_xpath(selectaday).click()
        time.sleep(5)
        print(today)
        environment.selecttimeslot(context)
        print("---------------------------")


@then(u'First session should be scheduled')
def step_impl(context):
    time.sleep(10)
    print("Its done")
