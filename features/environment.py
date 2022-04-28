import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb
from allure_commons.types import AttachmentType
import allure

def before_feature(context,feature):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)
    context.driver.delete_all_cookies()

    # options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=C:/Users/kanaka/AppData/Local/Google/Chrome/User")
    # chrome_driver_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    # context.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
#
# def after_feature(context,feature):
#     context.driver.quit()


def invokeloginpage(context):
    time.sleep(5)
    context.driver.get(gb.URL)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)



def selecttimeslot(context):
    context.driver.find_element_by_xpath("//label[text()=' 30 Minutes ']").click()
    time.sleep(5)
    count = 0
    if context.driver.find_element_by_xpath("//h6[text()='No free time available for selected day']").is_displayed():
        print("Coach is not available for selected day")
    else:
        try:
            for i in range(6):
                context.driver.find_element_by_xpath('//button[@aria-label="Previous"]').click()
                time.sleep(1)
        except:
            for i in range(6):
                context.driver.find_element_by_xpath('//button[@aria-label="Previous"]').click()
                time.sleep(1)

        time.sleep(5)

        try:
            context.driver.find_element_by_id("12:00 AM").click()
            count = count + 1
        except:
            print("12:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("12:30 AM").click()
            count = count + 1
        except:
            print("12:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("01:00 AM").click()
            count = count + 1
        except:
            print("01:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("01:30 AM").click()
            count = count + 1
        except:
            print("01:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("02:00 AM").click()
            count = count + 1
        except:
            print("02:00 AM coach is busy")

        time.sleep(3)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("02:30 AM").click()
            count = count + 1
        except:
            print("02:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("03:00 AM").click()
            count = count + 1
        except:
            print("03:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("03:30 AM").click()
            count = count + 1
        except:
            print("03:30 AM coach is busy")

        time.sleep(3)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("04:00 AM").click()
            count = count + 1
        except:
            print("04:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("04:30 AM").click()
            count = count + 1
        except:
            print("04:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("05:00 AM").click()
            count = count + 1
        except:
            print("05:00 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("05:30 AM").click()
            count = count + 1
        except:
            print("05:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("06:00 AM").click()
            count = count + 1
        except:
            print("06:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("06:30 AM").click()
            count = count + 1
        except:
            print("06:30 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("07:00 AM").click()
            count = count + 1
        except:
            print("07:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("07:30 AM").click()
            count = count + 1
        except:
            print("07:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("08:00 AM").click()
            count = count + 1
        except:
            print("08:00 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("08:30 AM").click()
            count = count + 1
        except:
            print("08:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("09:00 AM").click()
            count = count + 1
        except:
            print("09:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("09:30 AM").click()
            count = count + 1
        except:
            print("09:30 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("10:00 AM").click()
            count = count + 1
        except:
            print("10:00 AM coach is busy")

        try:
            context.driver.find_element_by_id("10:30 AM").click()
            count = count + 1
        except:
            print("10:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("11:00 AM").click()
            count = count + 1
        except:
            print("11:00 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("11:30 AM").click()
            count = count + 1
        except:
            print("11:30 AM coach is busy")

        try:
            context.driver.find_element_by_id("12:00 PM").click()
            count = count + 1
        except:
            print("12:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("12:30 PM").click()
            count = count + 1
        except:
            print("12:30 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("01:00 PM").click()
            count = count + 1
        except:
            print("01:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("01:30 PM").click()
            count = count + 1
        except:
            print("01:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("02:00 PM").click()
            count = count + 1
        except:
            print("02:00 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("02:30 PM").click()
            count = count + 1
        except:
            print("02:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("03:00 PM").click()
            count = count + 1
        except:
            print("03:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("03:30 PM").click()
            count = count + 1
        except:
            print("03:30 AM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("04:00 PM").click()
            count = count + 1
        except:
            print("04:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("04:30 PM").click()
            count = count + 1
        except:
            print("04:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("05:00 PM").click()
            count = count + 1
        except:
            print("05:00 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("05:30 PM").click()
            count = count + 1
        except:
            print("05:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("06:00 PM").click()
            count = count + 1
        except:
            print("06:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("06:30 PM").click()
            count = count + 1
        except:
            print("06:30 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("07:00 PM").click()
            count = count + 1
        except:
            print("07:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("07:30 PM").click()
            count = count + 1
        except:
            print("07:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("08:00 PM").click()
            count = count + 1
        except:
            print("08:00 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("08:30 PM").click()
            count = count + 1
        except:
            print("08:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("09:00 PM").click()
            count = count + 1
        except:
            print("09:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("09:30 PM").click()
            count = count + 1
        except:
            print("09:30 PM coach is busy")

        time.sleep(3)

        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        try:
            context.driver.find_element_by_id("10:00 PM").click()
            count = count + 1
        except:
            print("10:00 PM coach is busy")

        try:
            context.driver.find_element_by_id("10:30 PM").click()
            count = count + 1
        except:
            print("10:30 PM coach is busy")

        try:
            context.driver.find_element_by_id("11:00 PM").click()
            count = count + 1
        except:
            print("11:00 PM coach is busy")

        time.sleep(3)
        context.driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
        time.sleep(3)

        if count == 47:
            print("Coach is all day available")


def createevent(context):
    for i in range(1, 8):

        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = today.strftime("%b")  # int-stringconversion
        year = str(today.year)  # int-stringconversion

        startdate = month + " " + day + "," + " " + year  # gmaildateformat
        # enddate = month + " " + day + "," + " " + year   gmaildateformat
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
        context.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/span/span/span/div[2]").click()
        time.sleep(3)
        context.driver.find_element_by_xpath("//div[text()='Event']").click()
        time.sleep(10)
        context.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[1]/span/span").click()
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
    time.sleep(5)

    try:
        context.driver.find_element_by_id("12:00 AM").click()
        count = count + 1
    except:
        print("12:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("01:00 AM").click()
        count = count + 1
    except:
        print("01:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("02:00 AM").click()
        count = count + 1
    except:
        print("02:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("03:00 AM").click()
        count = count + 1
    except:
        print("03:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("04:00 AM").click()
        count = count + 1
    except:
        print("04:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("05:00 AM").click()
        count = count + 1
    except:
        print("05:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("06:00 AM").click()
        count = count + 1
    except:
        print("06:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("07:00 AM").click()
        count = count + 1
    except:
        print("07:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("08:00 AM").click()
        count = count + 1
    except:
        print("08:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("09:00 AM").click()
        count = count + 1
    except:
        print("09:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("10:00 AM").click()
        count = count + 1
    except:
        print("10:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("11:00 AM").click()
        count = count + 1
    except:
        print("11:00 AM coach is busy")

    try:
        context.driver.find_element_by_id("12:00 PM").click()
        count = count + 1
    except:
        print("12:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("01:00 PM").click()
        count = count + 1
    except:
        print("01:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("02:00 PM").click()
        count = count + 1
    except:
        print("02:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("03:00 PM").click()
        count = count + 1
    except:
        print("03:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("04:00 PM").click()
        count = count + 1
    except:
        print("04:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("05:00 PM").click()
        count = count + 1
    except:
        print("05:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("06:00 PM").click()
        count = count + 1
    except:
        print("06:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("07:00 PM").click()
        count = count + 1
    except:
        print("07:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("08:00 PM").click()
        count = count + 1
    except:
        print("08:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("09:00 PM").click()
        count = count + 1
    except:
        print("09:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("10:00 PM").click()
        count = count + 1
    except:
        print("10:00 PM coach is busy")

    try:
        context.driver.find_element_by_id("11:00 PM").click()
        count = count + 1

    except:
        print("11:00 PM coach is busy")

    if count == 24:
        print("Coach is all day available")

    if count == 0:
        print("Coach is not available for selected day")


def create_event_on_outlook_calendar(context):
    for i in range(1, 8):

        today = date.today() + timedelta(i)  # tommorrow date
        day = str(today.day)  # int-stringconversion
        month = str(today.month)  # int-stringconversion
        year = str(today.year)  # int-stringconversion

        startdate = month + "/" + day + "/" + year  # outlookdateformat
        enddate = month + "/" + day + "/" + year  # outlookdateformat
        title = ""
        starttime = ""
        endtime = ""

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

        context.driver.find_element_by_xpath("//span[text()='New event']").click()
        time.sleep(10)

        context.driver.find_element_by_xpath("//button[text()='More options']").click()
        time.sleep(10)

        context.driver.find_element_by_xpath("//input[@aria-label='Start date']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='Start date']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(Keys.CONTROL, 'a')
        context.driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(Keys.DELETE)
        context.driver.find_element_by_xpath("//input[@aria-label='Start date']").send_keys(startdate)
        time.sleep(5)

        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.CONTROL, 'a')
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.DELETE)
        context.driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(starttime)
        time.sleep(5)

        context.driver.find_element_by_xpath("//input[@aria-label='End date']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='End date']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(Keys.CONTROL, 'a')
        context.driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(Keys.DELETE)
        context.driver.find_element_by_xpath("//input[@aria-label='End date']").send_keys(enddate)
        time.sleep(5)

        context.driver.find_element_by_xpath("//input[@aria-label='End time']").click()
        context.driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(Keys.CONTROL, 'a')
        context.driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(Keys.DELETE)
        context.driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(endtime)
        time.sleep(5)

        context.driver.find_element_by_xpath("//input[@aria-label='Add details for the event']").send_keys(title)
        time.sleep(5)

        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        context.driver.find_element_by_xpath("//span[text()='Save']").click()
        time.sleep(5)
