import time
from datetime import date, timedelta
from features import myglobal as gb
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
driver.find_element_by_name("password").send_keys("Quantuvos@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(10)

# driver.find_element_by_id("identifierId").send_keys('automatecoach@gmail.com')
# driver.find_element_by_id("identifierNext").click()
# time.sleep(5)
# driver.find_element_by_name("password").send_keys('Kanaka@123')
# driver.find_element_by_id("passwordNext").click()
#
#
# today = date.today() + timedelta(1)  # tommorrow date
# day = str(today.day)  # int-stringconversion
# month = today.strftime("%b")  # int-stringconversion
# year = str(today.year)  # int-stringconversion
#
# startdate = month + " " + day + "," + " " + year  # gmaildateformat
# enddate = month + " " + day + "," + " " + year  # gmaildateformat
#
# title = "Single Event  7-8 am"
# starttime = "7.00am"
# endtime = "8.00am"
#
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div/span/span/span/div[2]").click()
# time.sleep(3)
# driver.find_element_by_xpath("//div[text()='Event']").click()
# time.sleep(10)
# driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[1]/span/span").click()
# time.sleep(3)
# driver.find_element_by_xpath("//input[@aria-label='Title']").send_keys(title)
# time.sleep(3)
# driver.find_element_by_id("xStDaIn").click()
# time.sleep(3)
# driver.find_element_by_id("xStDaIn").send_keys(Keys.DELETE)
# time.sleep(5)
# driver.find_element_by_id("xStDaIn").send_keys(startdate)
# time.sleep(3)
# driver.find_element_by_id("xStDaIn").send_keys(Keys.ENTER)
# driver.find_element_by_id("xStDaIn").send_keys(Keys.TAB)
# time.sleep(2)
#
# driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.DELETE)
# driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(starttime)
# driver.find_element_by_xpath("//input[@aria-label='Start time']").send_keys(Keys.TAB)
# time.sleep(5)
# driver.find_element_by_xpath("//input[@aria-label='End time']").send_keys(endtime)
# time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Save']").click()
# time.sleep(5)
#
#
# driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
# driver.maximize_window()
# time.sleep(5)
# driver.execute_script("window.open('about:blank','opsdashboard');")
# driver.switch_to.window("opsdashboard")
# driver.get(gb.URL)
# driver.maximize_window()
# time.sleep(10)
# driver.implicitly_wait(10)
# driver.find_element_by_name("email").send_keys("cahoyo3533@shirulo.com")
# driver.find_element_by_name("password").send_keys("Kanaka@123")
# driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
# time.sleep(10)
#
# time.sleep(5)
# driver.find_element_by_link_text("Sessions").click()
# time.sleep(10)
# today = date.today()
# day = str(today.day + 1)
# gmailtimeslot = "07.00 AM"
# checkevent = "//span[text()='" + day + "']"
# rightclick = driver.find_element_by_xpath(checkevent)
# actionChains = ActionChains(driver)
# actionChains.context_click(rightclick).perform()
#
# time.sleep(10)
#
# driver.find_element_by_xpath("/html/body/div[2]/div/div/context-menu-content/div/ul/li[2]/a/h5/span").click()
# time.sleep(15)
# today = date.today() + timedelta(1)  # tommorrow date
# day = str(today.day)  # int-stringconversion
# month = today.strftime("%b")  # int-stringconversion
# selectaday = "//span[text()='" + month + " " + day + "']"
# driver.find_element_by_xpath(selectaday).click()
#
#
# tmst = 7
# for i in range(12):
#     tmst = tmst+1
#     str = "0"+tmst+":00 AM"
#
#     timeslot = driver.find_element_by_id(str)
#     if timeslot.is_displayed():
#         pass
#     else:
#         print(str+"coach busy")
#
# tmst = 1
# for i in range(10):
#     tmst = tmst+1
#     str = "0"+tmst+":00 PM"
#
#     timeslot = driver.find_element_by_id(str)
#     if timeslot.is_displayed():
#         pass
#     else:
#         print(str+"coach busy")