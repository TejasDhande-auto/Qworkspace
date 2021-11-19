import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


@given(u'Open browser and hit the login URL')
def obhl(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)

    context.driver.get("https://platform-dev.quantuvos.com/login")
    context.driver.maximize_window()



@when(u'Enter client email "{email}" and password "{password}".')
def step_impl(context,email,password):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'Go to the session screen')
def step_impl(context):
    context.driver.find_element_by_link_text("Sessions").click()
    time.sleep(15)


@when(u'right click on one of the date')
def step_impl(context):
    rightclick = context.driver.find_element_by_xpath("/html/body/app-root/app-session/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/mwl-calendar-month-view/div/div/div[5]/div/mwl-calendar-month-cell[5]/div/div[1]/span[2]")
    actionChains = ActionChains(context.driver)
    actionChains.context_click(rightclick).perform()

    time.sleep(10)


@when(u'click on Schedule Session')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[2]/div/div/context-menu-content/div/ul/li[2]/a/h5/span").click()
    time.sleep(15)


@when(u'Select Date and time and click on save')
def step_impl(context):
    try:
        #context.driver.find_element_by_xpath("/html/body/app-root/app-session/div[1]/div[3]/div/div/div[2]/app-create-event/form/div[2]/div/div/ngx-slick-carousel/div/div/div[4]/div").click()
        context.driver.find_element_by_id("08:00 AM").click()
        context.driver.find_element_by_xpath("/html/body/app-root/app-session/div[1]/div[3]/div/div/div[2]/app-create-event/form/div[5]/button[2]").click()
        time.sleep(10)
    except:
        print("8.30 not available")
        context.driver.find_element_by_id("10:30 AM").click()
        context.driver.find_element_by_xpath("/html/body/app-root/app-session/div[1]/div[3]/div/div/div[2]/app-create-event/form/div[5]/button[2]").click()
        time.sleep(10)

@then(u'Sesion has been scheduled')
def step_impl(context):
    text = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]")
    if text == "Sessiom Created":
        print("Test case passed")
    context.driver.close()