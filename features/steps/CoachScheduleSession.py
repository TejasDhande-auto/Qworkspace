import time
from datetime import date,timedelta

from behave import *
from features import environment



@given(u'Coach should logged in with valid credential "{email}" , "{password}"')
def step_impl(context,email,password):
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
def step_impl(context,clientname):
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
def step_impl(context):

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

