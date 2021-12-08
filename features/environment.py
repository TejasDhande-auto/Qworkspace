import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from features  import myglobal as gb
from allure_commons.types import AttachmentType
import allure

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)


def after_all(context):
    context.driver.quit()


def invokeloginpage(context):
    time.sleep(5)
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def invoketempmailpage(context):
    time.sleep(5)
    context.driver.get(gb.TEMPURL)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def selecttimeslot(context):
    count = 0
    if context.driver.find_element_by_xpath("//h6[text()='No free time available for selected day']").is_displayed():
        print("Coach is all day busy")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    else:

        if context.driver.find_element_by_id("07:00 AM").is_displayed():
            count = count + 1
        else:
            print("07:00 AM coach is busy")

        if context.driver.find_element_by_id("07:30 AM").is_displayed():
            count = count + 1
        else:
            print("07:30 AM coach is busy")

        if context.driver.find_element_by_id("08:00 AM").is_displayed():
            count = count + 1
        else:
            print("08:00 AM coach is busy")

        if context.driver.find_element_by_id("08:30 AM").is_displayed():
            count = count + 1
        else:
            print("08:30 AM coach is busy")

        if context.driver.find_element_by_id("09:00 AM").is_displayed():
            count = count + 1
        else:
            print("09:00 AM coach is busy")

        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if context.driver.find_element_by_id("09:30 AM").is_displayed():
            count = count + 1
        else:
            print("09:30 AM coach is busy")

        if context.driver.find_element_by_id("10:00 AM").is_displayed():
            count = count + 1
        else:
            print("10:00 AM coach is busy")

        if context.driver.find_element_by_id("10:30 AM").is_displayed():
            count = count + 1
        else:
            print("10:30 AM coach is busy")

        if context.driver.find_element_by_id("11:00 AM").is_displayed():
            count = count + 1
        else:
            print("11:00 AM coach is busy")

        if context.driver.find_element_by_id("11:30 AM").is_displayed():
            count = count + 1
        else:
            print("11:30 AM coach is busy")

        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if context.driver.find_element_by_id("12:00 PM").is_displayed():
            count = count + 1
        else:
            print("12:00 PM coach is busy")

        if context.driver.find_element_by_id("12:30 PM").is_displayed():
            count = count + 1
        else:
            print("12:30 PM coach is busy")

        if context.driver.find_element_by_id("01:00 PM").is_displayed():
            count = count + 1
        else:
            print("01:00 PM coach is busy")

        if context.driver.find_element_by_id("01:30 PM").is_displayed():
            count = count + 1
        else:
            print("01:30 PM coach is busy")

        if context.driver.find_element_by_id("02:00 PM").is_displayed():
            count = count + 1
        else:
            print("02:00 PM coach is busy")

        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if context.driver.find_element_by_id("02:30 PM").is_displayed():
            count = count + 1
        else:
            print("02:30 PM coach is busy")

        if context.driver.find_element_by_id("03:00 PM").is_displayed():
            count = count + 1
        else:
            print("03:00 PM coach is busy")

        if context.driver.find_element_by_id("03:30 PM").is_displayed():
            count = count + 1
        else:
            print("03:30 AM coach is busy")

        if context.driver.find_element_by_id("04:00 PM").is_displayed():
            count = count + 1
        else:
            print("04:00 PM coach is busy")

        if context.driver.find_element_by_id("04:30 PM").is_displayed():
            count = count + 1
        else:
            print("04:30 PM coach is busy")

        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if context.driver.find_element_by_id("05:00 PM").is_displayed():
            count = count + 1
        else:
            print("05:00 PM coach is busy")

        if context.driver.find_element_by_id("05:30 PM").is_displayed():
            count = count + 1
        else:
            print("05:30 PM coach is busy")

        if context.driver.find_element_by_id("06:00 PM").is_displayed():
            count = count + 1
        else:
            print("06:00 PM coach is busy")

        if context.driver.find_element_by_id("06:30 PM").is_displayed():
            count = count + 1
        else:
            print("06:30 PM coach is busy")

        if context.driver.find_element_by_id("07:00 PM").is_displayed():
            count = count + 1
        else:
            print("07:00 PM coach is busy")

        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if context.driver.find_element_by_id("07:30 PM").is_displayed():
            count = count + 1
        else:
            print("07:30 PM coach is busy")

        if context.driver.find_element_by_id("08:00 PM").is_displayed():
            count = count + 1
        else:
            print("08:00 PM coach is busy")

        if context.driver.find_element_by_id("08:30 PM").is_displayed():
            count = count + 1
        else:
            print("08:30 PM coach is busy")

        if count == 28:
            print("Coach is all day available")


def createevent(context):
    for i in range(1, 8):

        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        year = str(today.year)  # int-stringconversion

        startdate = month + " " + day + "," + " " + year  # gmaildateformat
        #enddate = month + " " + day + "," + " " + year   gmaildateformat
        title = ""
        starttime = ""
        endtime = ""

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
        context.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div/span/span/span/div[2]").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//div[text()='Event']").click()
        time.sleep(10)
        context.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[1]/span/span").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//input[@aria-label='Title']").send_keys(title)
        time.sleep(3)
        context.driver.find_element_by_id("xStDaIn").click()
        time.sleep(3)
        context.driver.find_element_by_id("xStDaIn").send_keys(Keys.DELETE)
        time.sleep(5)
        context.driver.find_element_by_id("xStDaIn").send_keys(startdate)
        time.sleep(3)
        context.driver.find_element_by_id("xStDaIn").send_keys(Keys.ENTER)
        context.driver.find_element_by_id("xStDaIn").send_keys(Keys.TAB)
        time.sleep(2)

        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.DELETE)
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(starttime)
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.TAB)
        time.sleep(5)
        context.driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(endtime)
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath("//span[text()='Save']").click()
        time.sleep(5)

def selecttimeslotforfirstsession(context):
    count = 0
    if context.driver.find_element_by_id("07:00 AM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("07:00 AM coach is busy")

    if context.driver.find_element_by_id("08:00 AM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("8 am coach busy")

    if context.driver.find_element_by_id("09:00 AM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("9 am coach busy")

    if context.driver.find_element_by_id("10:00 AM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("10 am coach busy")

    if context.driver.find_element_by_id("11:00 AM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("11 am coach busy")

    if context.driver.find_element_by_id("12:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("12 am coach busy")

    if context.driver.find_element_by_id("01:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("01 pm coach busy")

    if context.driver.find_element_by_id("02:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("02 pm coach busy")

    if context.driver.find_element_by_id("03:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("03 pm coach busy")

    if context.driver.find_element_by_id("04:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("04 pm coach busy")

    if context.driver.find_element_by_id("05:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("05 pm coach busy")

    if context.driver.find_element_by_id("06:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("06 pm coach busy")

    if context.driver.find_element_by_id("07:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("07 pm coach busy")

    if context.driver.find_element_by_id("08:00 PM").is_displayed():
        time.sleep(2)
        count = count + 1
    else:
        print("08 pm coach busy")

    if count == 14:
        print("Coach is all day available")

    if count == 0:
        print("Coach is all day busy")
