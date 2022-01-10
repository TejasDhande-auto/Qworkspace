from behave import *
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
import allure
import time
import features.steps.myglobal as gb

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://platform-dev.quantuvos.com/login")

driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("cohiy57225@kyrescu.com")
driver.find_element_by_name("password").send_keys("Qwerty@123")
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[2]/div/div[1]/input").send_keys("ha")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[2]/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@data-value='Albania']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Self']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/input").send_keys("Automation")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
time.sleep(3)
driver.find_element_by_name("data[PhoneNumber]").send_keys("1234567890")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[2]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]").click()
driver.find_element_by_xpath("//div[@data-value='Female']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]").click()
driver.find_element_by_xpath("//div[@data-value='25-35']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@data-value='Married']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[5]/div[1]/div[2]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[6]/div[1]/div[2]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[8]/div[1]/div[2]/label/input").click()
driver.execute_script("window.scrollTo(500, document.body.scrollHeight)")
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[7]/div[1]/input").send_keys("Master in Automation")
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Submit']").click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/app-root/app-coach-calendar-access/div[1]/div[3]/button/span").click()
time.sleep(5)


