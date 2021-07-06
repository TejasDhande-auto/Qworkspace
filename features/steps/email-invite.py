from behave import *
from selenium import webdriver

@given('Open Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('Navigate to the page')
def step_impl(context):
    context.driver.get("https://platform-dev.quantuvos.com/set-password/client/RtvG1yL_aCxoQAL")
    context.driver.maximize_window()

@when('Enter password "{pwd}" and confirm password "{cpwd}"')
def step_impl(context,pwd,cpwd):
    context.driver.find_element_by_id("password").send_keys(pwd)
    context.driver.find_element_by_id("confirmPassword").send_keys(cpwd)


@then('password save successfully')
def step_impl(context):
    try:
        context.driver.find_element_by_id("btnNext").click()

    except:
        context.driver.close
        assert False, "Test Failed"

    assert True, "Test Passed"
    context.driver.close





