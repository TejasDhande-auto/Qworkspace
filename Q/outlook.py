import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date, timedelta
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)


driver.execute_script("window.open('about:blank','1');")
driver.switch_to.window("1")
driver.execute_script("document.body.style.zoom='zoom 75%'")
driver.get("https://outlook.live.com/calendar/0/view/month")

time.sleep(10)
driver.find_element_by_link_text("Sign in").click()
time.sleep(5)
driver.find_element_by_id('i0116').send_keys("automatecoach@outlook.com")
time.sleep(5)
driver.find_element_by_id('idSIButton9').click()
time.sleep(5)
driver.find_element_by_id('i0118').send_keys("Kanaka@123")
time.sleep(3)
driver.find_element_by_id('idSIButton9').click()
time.sleep(3)
driver.find_element_by_id('idSIButton9').click()
time.sleep(10)

for i in range(1, 8):

    today = date.today() + timedelta(i)  # tommorrow date
    day = str(today.day)  # int-stringconversion
    month = str(today.month)  # int-stringconversion
    year = str(today.year)  # int-stringconversion

    startdate = month+"/"+day+"/"+year  # outlookdateformat
    enddate = month+"/"+day+"/"+year # outlookdateformat
    title=""
    starttime=""
    endtime=""



    if i == 1:
        title = "Single Event  7-8  AM"
        starttime = "7:00 AM"
        endtime = "8:00 AM"

    elif i == 2:
        title = "Single Event  8-9  AM"
        starttime = "8:00 AM"
        endtime = "9:00 AM"

    elif i == 3:
        title = "Single Event  9-10  AM"
        starttime = "9:00 AM"
        endtime = "10:00 AM"

    elif i == 4:
        title = "Single Event  10-11  AM"
        starttime = "10:00 AM"
        endtime = "11:00 AM"

    elif i == 5:
        title = "Single Event  10 AM-5 PM"
        starttime = "10:00 AM"
        endtime = "5:00 PM"

    elif i == 6:
        title = "Single Event  7 AM-9 PM"
        starttime = "7:00 AM"
        endtime = "9:00 PM"

    elif i == 7:
        title = "Single Event  7 AM-7 PM"
        starttime = "7:00 AM"
        endtime = "7:00 PM"



    time.sleep(5)


    driver.find_element_by_xpath("//span[text()='New event']").click()
    time.sleep(10)

    driver.find_element_by_xpath("//button[text()='More options']").click()
    time.sleep(10)

    driver.find_element_by_xpath("//input[@aria-label='Start date']").click()
    driver.find_element_by_xpath("//input[@aria-label='Start date']").click()
    driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(Keys.DELETE)
    driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(startdate)
    time.sleep(5)

    driver.find_element_by_xpath("//input[@aria-label='Start time']").click()
    driver.find_element_by_xpath("//input[@aria-label='Start time']").click()
    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.DELETE)
    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(starttime)
    time.sleep(5)

    driver.find_element_by_xpath("//input[@aria-label='End date']").click()
    driver.find_element_by_xpath("//input[@aria-label='End date']").click()
    driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(Keys.DELETE)
    driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(enddate)
    time.sleep(5)

    driver.find_element_by_xpath("//input[@aria-label='End time']").click()
    driver.find_element_by_xpath("//input[@aria-label='End time']").click()
    driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(Keys.DELETE)
    driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(endtime)
    time.sleep(5)

    driver.find_element_by_xpath("//input[@aria-label='Add details for the event']").send_keys(title)
    time.sleep(5)

    driver.find_element_by_xpath("//span[text()='Save']").click()
    time.sleep(5)
