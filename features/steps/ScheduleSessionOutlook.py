import time
from datetime import date, timedelta
from behave import *

from selenium.webdriver.common.keys import Keys
from features import environment
from features import myglobal as gb
from selenium.webdriver import ActionChains

@given(u': Outlook Coach should busy on next seven days at different time login as "{email}","{password}"')
def step_impl(context,email,password):
    context.driver.execute_script("window.open('about:blank','1');")
    context.driver.switch_to.window("1")
    context.driver.execute_script("document.body.style.zoom='zoom 75%'")
    context.driver.get("https://outlook.live.com/calendar/0/view/month")

    time.sleep(10)
    context.driver.find_element_by_link_text("Sign in").click()
    time.sleep(5)
    context.driver.find_element_by_id('i0116').send_keys(email)
    time.sleep(5)
    context.driver.find_element_by_id('idSIButton9').click()
    time.sleep(5)
    context.driver.find_element_by_id('i0118').send_keys(password)
    time.sleep(3)
    context.driver.find_element_by_id('idSIButton9').click()
    time.sleep(3)
    context.driver.find_element_by_id('idSIButton9').click()
    time.sleep(10)
    environment.create_event_on_outlook_calendar(context)


@then(u': If proper then display better')
def step_impl(context):
    print("Better")
