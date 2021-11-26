import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://calendar.google.com/calendar/u/0/r?tab=mc&pli=1")

driver.find_element_by_id("identifierId").send_keys('automatecoach@gmail.com')
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys('Kanaka@123')
driver.find_element_by_id("passwordNext").click()
for i in range(1, 8):

    today = date.today() + timedelta(i)  # tommorrow date
    day = str(today.day)  # int-stringconversion
    month = today.strftime("%b")  # int-stringconversion
    year = str(today.year)  # int-stringconversion

    startdate = month + " " + day + "," + " " + year  # gmaildateformat
    enddate = month + " " + day + "," + " " + year  # gmaildateformat
    title=""
    starttime=""
    endtime=""


    if i == 1:
        title = "Single Event  7-8 am"
        starttime = "7.00am"
        endtime = "8.00am"

    elif i == 2:
        title = "Single Event  8-9 am"
        starttime = "8.00am"
        endtime = "9.00am"

    elif i == 3:
        title = "Single Event  9-10 am"
        starttime = "9.00am"
        endtime = "10.00am"

    elif i == 4:
        title = "Single Event  10-11 am"
        starttime = "10.00am"
        endtime = "11.00am"

    elif i == 5:
        title = "Single Event  10am-5pm"
        starttime = "10.00am"
        endtime = "5.00pm"

    elif i == 6:
        title = "Single Event  7am-9pm"
        starttime = "7.00am"
        endtime = "9.00pm"

    elif i == 7:
        title = "Single Event  7am-7pm"
        starttime = "7.00am"
        endtime = "7.00pm"



    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div/span/span/span/div[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[text()='Event']").click()
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[1]/span/span").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@aria-label='Title']").send_keys(title)
    time.sleep(3)
    driver.find_element_by_id("xStDaIn").click()
    time.sleep(3)
    driver.find_element_by_id("xStDaIn").send_keys(Keys.DELETE)
    time.sleep(5)
    driver.find_element_by_id("xStDaIn").send_keys(startdate)
    time.sleep(3)
    driver.find_element_by_id("xStDaIn").send_keys(Keys.ENTER)
    driver.find_element_by_id("xStDaIn").send_keys(Keys.TAB)
    time.sleep(2)

    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.DELETE)
    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(starttime)
    driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.TAB)
    time.sleep(5)
    driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(endtime)
    time.sleep(3)
    driver.find_element_by_xpath("//span[text()='Save']").click()
    time.sleep(5)
