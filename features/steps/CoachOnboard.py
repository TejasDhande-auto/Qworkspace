from behave import *
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
import time
from features import myglobal as gb

@when(u': Send an invitation to coach (name="{name}",email="{email}")')

def step_impl(context,name,email):
    context.driver.get(gb.URL)
    context.driver.maximize_window()

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(gb.opsemail)
    context.driver.find_element_by_name("password").send_keys(gb.opspassword)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)

    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(3)
    context.driver.find_element_by_id("coachtype").click()
    time.sleep(5)
    context.driver.find_element_by_name("coachfirstname").send_keys(name)
    context.driver.find_element_by_name("coachlastname").send_keys("Automate")
    context.driver.find_element_by_name("coachemail").send_keys(email)
    time.sleep(5)
    context.driver.find_element_by_id("coachbtn").click()
    time.sleep(10)


@when(u': Complete the coach onboarding process (email="{email}")')

def step_impl(context,email):
    try:
        context.driver.switch_to.window("Mail")

    except:
        context.driver.execute_script("window.open('about:blank','Mail');")
        context.driver.switch_to.window("Mail")
        context.driver.get("https://outlook.live.com/mail")
        time.sleep(10)
        context.driver.find_element_by_link_text("Sign in").click()
        time.sleep(5)

        context.driver.find_element_by_id('i0116').send_keys("qtestcoach@outlook.com")
        time.sleep(5)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(10)
        context.driver.find_element_by_xpath('//input[@type="password"]').send_keys("Kanaka@123")
        time.sleep(3)
        context.driver.find_element_by_id('idSIButton9').click()
        time.sleep(5)
        context.driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(10)
        try:
            context.driver.find_element_by_xpath(
                "/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]").click()
            time.sleep(2)
        except:
            pass

    # First mail
    time.sleep(10)
    context.driver.find_element_by_xpath("(//span[text()='Welcome to Quantuvos!'])[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Start']").click()
    context.driver.switch_to.window(context.driver.window_handles[2])
    time.sleep(3)
    context.driver.find_element_by_xpath('//input[@id="email"]').send_keys(email)
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

    context.driver.switch_to.window("Mail")
    time.sleep(3)
    context.driver.find_element_by_xpath("(//span[text()='Please confirm your email'])[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[text()='Confirm']").click()
    context.driver.switch_to.window(context.driver.window_handles[3])

    time.sleep(3)
    context.driver.find_element_by_xpath('//input[@name="password"]').send_keys(gb.password)
    context.driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(gb.password)

    time.sleep(3)
    context.driver.find_element_by_id("btnNext").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(gb.password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)

    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[2]/button").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//div[@data-value='Albania']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()='Self']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/input").send_keys("Automation")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(3)
    context.driver.find_element_by_name("data[PhoneNumber]").send_keys("1234567890")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]").click()
    context.driver.find_element_by_xpath("//div[@data-value='Female']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]").click()
    context.driver.find_element_by_xpath("//div[@data-value='25-35']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[3]/div[1]/div[1]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[4]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//div[@data-value='Married']").click()
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[5]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[6]/div[1]/div[2]/label/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[8]/div[1]/div[2]/label/input").click()
    context.driver.execute_script("window.scrollTo(500, document.body.scrollHeight)")
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/ul/li[3]/button").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("/html/body/app-root/app-coachform/div[4]/div/formio/div/div/div/div/div/div[7]/div[1]/input").send_keys("Master in Automation")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(5)

@then(u': Coach dashboard should be open')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)

