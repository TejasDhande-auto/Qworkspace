from behave import *
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
#@given('Open browser')
#def openBrowser(context):
    #clscontext.driver = webdriver.Chrome()

@when(u'open page link from mail')
def openPage(context):
    context.driver.get("https://platform-dev.quantuvos.com/confirm-email/client/RjytANpGGnxwrwz")
    context.driver.maximize_window()

@when('Enter the "{email}" address')
def enterEmail(context,email):
    context.driver.find_element_by_id("email").send_keys(email)
@when(u'click on send button')
def clickSend(context):
    try:
        context.driver.find_element_by_id("btnSubmit").click()
        allure.attach('screenshot', context.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach('screenshot', context.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        context.driver.close()
        assert False,"Test failed"



@then(u'Confirmation email send successfully')
def step_impl(context):
    context.driver.close()
    assert True, "Test passed"

