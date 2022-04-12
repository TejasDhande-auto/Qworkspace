import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver

from selenium.webdriver import ActionChains

from features import environment

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("mabixep475@gyn5.com")
driver.find_element_by_name("password").send_keys("Qwerty@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(5)


driver.find_element_by_link_text("Sessions").click()
time.sleep(3)
today = date.today()
print(today)
day = str(today.day + 1)
print(day)
gmailtimeslot = "07.00 AM"
checkevent = "//span[text()='" + day + "']"
time.sleep(3)
#driver.find_element_by_xpath(checkevent).click()



rightclick = driver.find_element_by_xpath(checkevent)
action = ActionChains(driver)
action.context_click(rightclick).perform()

time.sleep(2)
driver.find_element_by_xpath("//span[text()='Schedule a Session']").click()
time.sleep(5)
# for i in range(1, 8):
#     today = date.today() + timedelta(i)  # tommorrow date
#     day = str(today.day)  # int-stringconversion
#     month = today.strftime("%b")  # int-stringconversion
#     selectaday = "//span[text()='" + month + " " + day + "']"
#     time.sleep(2)
#     driver.find_element_by_xpath(selectaday).click()
# time.sleep(5)
# print(today)

print("---------------------------")
driver.find_element_by_xpath("//label[text()=' 30 Minutes ']").click()
time.sleep(5)
count = 0
if driver.find_element_by_xpath("//h6[text()='No free time available for selected day']").is_displayed():
     print("Coach is not available for selected day")
else:
        
    for i in range(6):
        driver.find_element_by_xpath('//button[@aria-label="Previous"]').click()
        time.sleep(1)

    time.sleep(5)

    try:
        driver.find_element_by_id("12:00 AM").click()
        count = count + 1
    except:
        print("12:00 AM coach is busy")

    try:
         driver.find_element_by_id("12:30 AM").click()
         count = count + 1
    except:
        print("12:30 AM coach is busy")

    try:
         driver.find_element_by_id("01:00 AM").click()
         count = count + 1
    except:
        print("01:00 AM coach is busy")

    try:
         driver.find_element_by_id("01:30 AM").click()
         count = count + 1
    except:
        print("01:30 AM coach is busy")

    try:
         driver.find_element_by_id("02:00 AM").click()
         count = count + 1
    except:
        print("02:00 AM coach is busy")

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("02:30 AM").click()
         count = count + 1
    except:
        print("02:30 AM coach is busy")

    try:
         driver.find_element_by_id("03:00 AM").click()
         count = count + 1
    except:
        print("03:00 AM coach is busy")

    try:
         driver.find_element_by_id("03:30 AM").click()
         count = count + 1
    except:
        print("03:30 AM coach is busy")

    time.sleep(3)    
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("04:00 AM").click()
         count = count + 1
    except:
        print("04:00 AM coach is busy")

    try:
         driver.find_element_by_id("04:30 AM").click()
         count = count + 1
    except:
        print("04:30 AM coach is busy")

    try:
         driver.find_element_by_id("05:00 AM").click()
         count = count + 1
    except:
        print("05:00 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("05:30 AM").click()
         count = count + 1
    except:
        print("05:30 AM coach is busy")

    try:
         driver.find_element_by_id("06:00 AM").click()
         count = count + 1
    except:
        print("06:00 AM coach is busy")

    try:
         driver.find_element_by_id("06:30 AM").click()
         count = count + 1
    except:
        print("06:30 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("07:00 AM").click()
         count = count + 1
    except:
        print("07:00 AM coach is busy")

    try:
         driver.find_element_by_id("07:30 AM").click()
         count = count + 1
    except:
        print("07:30 AM coach is busy")

    try:
         driver.find_element_by_id("08:00 AM").click()
         count = count + 1
    except:
        print("08:00 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("08:30 AM").click()
         count = count + 1
    except:
        print("08:30 AM coach is busy")

    try:
         driver.find_element_by_id("09:00 AM").click()
         count = count + 1
    except:
        print("09:00 AM coach is busy")

    try:
         driver.find_element_by_id("09:30 AM").click()
         count = count + 1
    except:
        print("09:30 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("10:00 AM").click()
         count = count + 1
    except:
        print("10:00 AM coach is busy")

    try:
         driver.find_element_by_id("10:30 AM").click()
         count = count + 1
    except:
        print("10:30 AM coach is busy")

    try:
         driver.find_element_by_id("11:00 AM").click()
         count = count + 1
    except:
        print("11:00 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("11:30 AM").click()
         count = count + 1
    except:
        print("11:30 AM coach is busy")

    try:
         driver.find_element_by_id("12:00 PM").click()
         count = count + 1
    except:
        print("12:00 PM coach is busy")

    try:
         driver.find_element_by_id("12:30 PM").click()
         count = count + 1
    except:
        print("12:30 PM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("01:00 PM").click()
         count = count + 1
    except:
        print("01:00 PM coach is busy")

    try:
         driver.find_element_by_id("01:30 PM").click()
         count = count + 1
    except:
        print("01:30 PM coach is busy")

    try:
         driver.find_element_by_id("02:00 PM").click()
         count = count + 1
    except:
        print("02:00 PM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
         driver.find_element_by_id("02:30 PM").click()
         count = count + 1
    except:
        print("02:30 PM coach is busy")

    try:
         driver.find_element_by_id("03:00 PM").click()
         count = count + 1
    except:
        print("03:00 PM coach is busy")

    try:
         driver.find_element_by_id("03:30 PM").click()
         count = count + 1
    except:
        print("03:30 AM coach is busy")

    time.sleep(3)
     
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
        driver.find_element_by_id("04:00 PM").click()
        count = count + 1
    except:
        print("04:00 PM coach is busy")

    try:
        driver.find_element_by_id("04:30 PM").click()
        count = count + 1
    except:
        print("04:30 PM coach is busy")

    try:
        driver.find_element_by_id("05:00 PM").click()
        count = count + 1
    except:
        print("05:00 PM coach is busy")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
        driver.find_element_by_id("05:30 PM").click()
        count = count + 1
    except:
        print("05:30 PM coach is busy")

    try:
        driver.find_element_by_id("06:00 PM").click()
        count = count + 1
    except:
        print("06:00 PM coach is busy")

    try:
        driver.find_element_by_id("06:30 PM").click()
        count = count + 1
    except:
        print("06:30 PM coach is busy")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
        driver.find_element_by_id("07:00 PM").click()
        count = count + 1
    except:
        print("07:00 PM coach is busy")

    try:
        driver.find_element_by_id("07:30 PM").click()
        count = count + 1
    except:
        print("07:30 PM coach is busy")

    try:
        driver.find_element_by_id("08:00 PM").click()
        count = count + 1
    except:
        print("08:00 PM coach is busy")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
        driver.find_element_by_id("08:30 PM").click()
        count = count + 1
    except:
        print("08:30 PM coach is busy")

    try:
        driver.find_element_by_id("09:00 PM").click()
        count = count + 1
    except:
        print("09:00 PM coach is busy")

    try:
        driver.find_element_by_id("09:30 PM").click()
        count = count + 1
    except:
        print("09:30 PM coach is busy")

    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    try:
        driver.find_element_by_id("10:00 PM").click()
        count = count + 1
    except:
        print("10:00 PM coach is busy")

    try:
        driver.find_element_by_id("10:30 PM").click()
        count = count + 1
    except:
        print("10:30 PM coach is busy")

    try:
        driver.find_element_by_id("11:00 PM").click()
        count = count + 1
    except:
        print("11:00 PM coach is busy")

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="slick-carousel"]/button[2]').click()
    time.sleep(3)

    if count == 47:
        print("Coach is all day available")