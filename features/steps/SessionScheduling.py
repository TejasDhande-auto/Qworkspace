import time

import allure
from behave import *
from selenium.webdriver import ActionChains

from features import environment
from datetime import date, timedelta


@given(u'Client should logged in with valid credential "{email}" , "{password}"')
def clientlogin(context,email,password):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'Schedule Session with coach')
def clientschedulesession(context):
    time.sleep(5)
    context.driver.find_element_by_link_text("Sessions").click()
    time.sleep(3)
    today = date.today()
    print(today)
    day = str(today.day + 1)
    print(day)
    gmailtimeslot = "07.00 AM"
    checkevent = "//span[text()='"+day+"']"
    time.sleep(5)
    rightclick = context.driver.find_element_by_xpath(checkevent)
    action = ActionChains(context.driver)
    action.context_click(rightclick).perform()

    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Schedule a Session']").click()
    time.sleep(5)
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


@given(u'Coach should logged in with valid credential "{email}" , "{password}"')
def coachlogin(context,email,password):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(20)
    if context.driver.find_element_by_xpath('//*[@id="#postSurveyPOPUP"]/div/div/div[2]/button').is_displayed():
        context.driver.find_element_by_xpath('//*[@id="#postSurveyPOPUP"]/div/div/div[2]/button').click()

    context.driver.find_element_by_xpath("//span[text()='Clients']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[3]/span/span").click()
    time.sleep(3)


@when(u'Schedule session with client "{clientname}"')
def searchforclient(context,clientname):
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
        clientname)
    time.sleep(4)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-client-listing/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//span[text()='SCHEDULE +']").click()
    time.sleep(10)


@then(u'Session scheduled with client')
def coachschedulesession(context):

    for i in range (1,8):
        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        selectaday = "//span[text()='" + month + " " + day + "']"
        time.sleep(10)
        context.driver.find_element_by_xpath(selectaday).click()
        time.sleep(5)
        print(today)
        environment.selecttimeslot(context)
        print("---------------------------")


@given(u'Operation person should logged in with valid credential "{email}" , "{password}"')
def opslogin(context,email,password):
    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)

    time.sleep(10)
    context.driver.find_element_by_xpath('//*[@id="opt-clientsid"]/span').click()
    time.sleep(20)


@when(u'Schedule session with the client "{clientname}"')
def searchforclientbyops(context,clientname):
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
        clientname)
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Schedule Session ']").click()

@then(u'Session scheduled for client and coach')
def Opsschedulesession(context):

    for i in range (1,8):
        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        selectaday = "//span[text()='" + month + " " + day + "']"
        time.sleep(15)
        context.driver.find_element_by_xpath(selectaday).click()
        time.sleep(10)
        print(today)
        environment.selecttimeslot(context)
        print("---------------------------")

