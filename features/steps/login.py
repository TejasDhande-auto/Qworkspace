import time

from Pages.Loginpage import Loginpage
from behave import *
from selenium import webdriver


@given(u': Login screen should display')
def step_impl(context):
    context.driver.get("https://platform-uat.quantuvos.com/login")
    time.sleep(5)

@when(u': Enter username "{email}"an and password "{password}" and click on login')
def step_impl(context,email,password):
    login = Loginpage(context.driver)
    login.Enteremailadress(email)
    login.Enterpassword(password)
    time.sleep(5)
    login.clickonlogin()
    time.sleep(5)


@then(u': Home page shuld display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Home page shuld display')

