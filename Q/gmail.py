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
time.sleep(20)
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("mabixep475@gyn5.com")
driver.find_element_by_name("password").send_keys("Qwerty@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(10)

time.sleep(5)
driver.find_element_by_link_text("Sessions").click()
time.sleep(10)
today = date.today()
print(today)
day = str(today.day + 1)
print(day)
gmailtimeslot = "07.00 AM"
checkevent = "//span[text()='" + day + "']"
time.sleep(5)
#driver.find_element_by_xpath(checkevent).click()
time.sleep(10)


rightclick = driver.find_element_by_xpath(checkevent)
action = ActionChains(driver)
action.context_click(rightclick).perform()

time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div/context-menu-content/div/ul/li[2]/a/h5").click()
time.sleep(10)
for i in range(1, 8):
    today = date.today() + timedelta(i)  # tommorrow date
    day = str(today.day)  # int-stringconversion
    month = today.strftime("%b")  # int-stringconversion
    selectaday = "//span[text()='" + month + " " + day + "']"
    time.sleep(2)
    driver.find_element_by_xpath(selectaday).click()
time.sleep(5)
print(today)
environment.selecttimeslot(driver)
print("---------------------------")
