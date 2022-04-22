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
# driver.execute_script("document.body.style.zoom='zoom 75%'")
driver.get("https://outlook.live.com/mail")


time.sleep(10)
driver.find_element_by_link_text("Sign in").click()
time.sleep(5)

driver.find_element_by_id('i0116').send_keys("qtestclient@outlook.com")
time.sleep(5)
driver.find_element_by_id('idSIButton9').click()
time.sleep(10)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("Kanaka@123")
time.sleep(3)
driver.find_element_by_id('idSIButton9').click()
time.sleep(5)
driver.find_element_by_xpath('//input[@type="submit"]').click()
time.sleep(10)
#First mail
try:
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]").click()
    time.sleep(2)
except:
    pass

driver.find_element_by_xpath("(//span[text()='Welcome to Quantuvos!'])[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Start']").click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('//input[@id="email"]').send_keys("Qtestclientt+1@outlook.com")
time.sleep(3)
driver.find_element_by_id('btnSubmit').click()
time.sleep(5)


time.sleep(5)
driver.find_element_by_xpath("(//span[text()='Please confirm your email'])[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Confirm']").click()
time.sleep(5)

