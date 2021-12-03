import time
from datetime import date, timedelta
from behave import *

from selenium.webdriver.common.keys import Keys
from features import environment
from features import myglobal as gb
from selenium.webdriver import ActionChains

@given(u': Coach should busy on next seven days at different time')
def Createeventoncoachcalendar(context):
    context.driver.get("https://calendar.google.com/calendar/u/0/r?tab=mc&pli=1")

    context.driver.find_element_by_id("identifierId").send_keys('automatecoach@gmail.com')
    context.driver.find_element_by_id("identifierNext").click()
    time.sleep(5)
    context.driver.find_element_by_name("password").send_keys('Kanaka@123')
    context.driver.find_element_by_id("passwordNext").click()
    time.sleep(10)
    environment.createevent(context)
    time.sleep(10)

@when(u': Client will check coach availability')
def Checktimeslots(context):
    context.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    context.driver.maximize_window()
    time.sleep(5)

    context.driver.execute_script("window.open('about:blank','clientdashboard');")
    context.driver.switch_to.window("clientdashboard")
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    time.sleep(10)

    environment.invokeloginpage(context)
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys("cahoyo3533@shirulo.com")
    context.driver.find_element_by_name("password").send_keys("Kanaka@123")
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)

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

    context.driver.find_element_by_xpath(
        "/html/body/div[2]/div/div/context-menu-content/div/ul/li[2]/a/h5/span").click()
    time.sleep(10)
    for i in range(1, 8):
        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        year = today.year
        selectaday = "//span[text()='" + month + " " + day + "']"
        time.sleep(2)
        context.driver.find_element_by_xpath(selectaday).click()
        time.sleep(5)
        print(print(month,day,",",year))
        environment.selecttimeslot(context)
        print("---------------------------")

@then(u': If proper then display good')
def Alldone(context):
    print("Good")