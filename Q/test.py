import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)


driver.execute_script("window.open('about:blank','forthtab');")
driver.switch_to.window("forthtab")
driver.get('https://platform-dev.quantuvos.com/login')
driver.maximize_window()
time.sleep(10)

driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("gejoti6583@smuvaj.com")
driver.find_element_by_name("password").send_keys("Qwerty@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[2]/div[3]/div/div[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-select-coach/div[1]/div/div[2]/div[3]/button/span").click()
time.sleep(5)
try:
 driver.find_element_by_id("07:00 AM").click()
 time.sleep(2)
except Exception:
    print("7 am coach busy")

try:
 driver.find_element_by_id("08:00 AM").click()
 time.sleep(2)
except Exception:
    print("8 am coach busy")

try:
 driver.find_element_by_id("09:00 AM").click()
 time.sleep(2)
except Exception:
    print("9 am coach busy")

try:
 driver.find_element_by_id("10:00 AM").click()
 time.sleep(2)
except Exception:
    print("10 am coach busy")

try:
 driver.find_element_by_id("11:00 AM").click()
 time.sleep(2)
except Exception:
    print("11 am coach busy")

try:
 driver.find_element_by_id("12:00 PM").click()
 time.sleep(2)
except Exception:
    print("12 am coach busy")

try:
 driver.find_element_by_id("01:00 PM").click()
 time.sleep(2)
except Exception:
    print("01 pm coach busy")

try:
 driver.find_element_by_id("02:00 PM").click()
 time.sleep(2)
except Exception:
    print("02 pm coach busy")

try:
 driver.find_element_by_id("03:00 PM").click()
 time.sleep(2)
except Exception:
    print("03 pm coach busy")

try:
 driver.find_element_by_id("04:00 PM").click()
 time.sleep(2)
except Exception:
    print("04 pm coach busy")

try:
 driver.find_element_by_id("05:00 PM").click()
 time.sleep(2)
except Exception:
    print("05 pm coach busy")

try:
 driver.find_element_by_id("06:00 PM").click()
 time.sleep(2)
except Exception:
    print("06 pm coach busy")

try:
 driver.find_element_by_id("07:00 PM").click()
 time.sleep(2)
except Exception:
    print("07 pm coach busy")

except Exception:
    print("08 pm coach busy")
try:
 driver.find_element_by_id("08:00 PM").click()
 time.sleep(2)

driver.find_element_by_xpath("/html/body/app-root/app-weekly-calendar/div[3]/div/div[1]/form/div[3]/button/span").click()
time.sleep(15)
driver.find_element_by_xpath("/html/body/app-root/app-weekly-calendar/div[3]/div/div[2]/div/div/div[2]/button").click()
time.sleep(6)