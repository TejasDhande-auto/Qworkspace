import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from features import myglobal as gb

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)

driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.open('about:blank','coachdashboard');")
driver.switch_to.window("coachdashboard")
driver.get(gb.URL)
driver.maximize_window()
time.sleep(10)
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
driver.find_element_by_name("password").send_keys("Quantuvos@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="opt-clientsid"]/span').click()
time.sleep(20)
driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys("Mabixep")
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Schedule Session ']").click()

today = date.today() + timedelta(1)  # tommorrow date
day = str(today.day)  # int-stringconversion
month = today.strftime("%b")  # int-stringconversion
year= today.year
selectaday = "//span[text()='" + month + " " + day + "']"
print(month,day,",",year)
driver.find_element_by_xpath(selectaday).click()
time.sleep(7)
driver.find_element_by_xpath("//label[text()=' 30 Minutes ']").click()
time.sleep(3)

if driver.find_element_by_xpath("//h6[text()='No free time available for selected day']").is_displayed():
    print("Coach is all day busy")




if driver.find_element_by_id("09:00 AM").is_displayed():
    pass
else:
    print("09:00 AM coach is busy")

time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(3)

if driver.find_element_by_id("09:30 AM").is_displayed():
    pass
else:
    print("09:30 AM coach is busy")

if driver.find_element_by_id("10:00 AM").is_displayed():
    pass
else:
    print("10:00 AM coach is busy")

if driver.find_element_by_id("10:30 AM").is_displayed():
    pass
else:
    print("10:30 AM coach is busy")

if driver.find_element_by_id("11:00 AM").is_displayed():
    pass
else:
    print("11:00 AM coach is busy")

time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(3)

if driver.find_element_by_id("11:30 AM").is_displayed():
    pass
else:
    print("11:30 AM coach is busy")

if driver.find_element_by_id("12:00 PM").is_displayed():
    pass
else:
    print("12:00 PM coach is busy")

if driver.find_element_by_id("12:30 PM").is_displayed():
    pass
else:
    print("12:30 PM coach is busy")

if driver.find_element_by_id("01:00 PM").is_displayed():
    pass
else:
    print("01:00 PM coach is busy")

if driver.find_element_by_id("01:30 PM").is_displayed():
    pass
else:
    print("01:30 PM coach is busy")

time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(3)

if driver.find_element_by_id("02:00 PM").is_displayed():
    pass
else:
    print("02:00 PM coach is busy")

if driver.find_element_by_id("02:30 PM").is_displayed():
    pass
else:
    print("02:30 PM coach is busy")

if driver.find_element_by_id("03:00 PM").is_displayed():
    pass
else:
    print("03:00 PM coach is busy")

if driver.find_element_by_id("03:30 PM").is_displayed():
    pass
else:
    print("03:30 AM coach is busy")

if driver.find_element_by_id("04:00 PM").is_displayed():
    pass
else:
    print("04:00 PM coach is busy")

time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(3)

if driver.find_element_by_id("04:30 PM").is_displayed():
    pass
else:
    print("04:30 PM coach is busy")



