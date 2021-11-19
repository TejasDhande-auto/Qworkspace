import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver


@given(u'Hit the Chrome browser')
def HitBrowser(context):
    #context.driver = webdriver.Firefox()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    context.driver = uc.Chrome(options=options)
    #driver.get('https://bet365.com')
    #context.driver.get(petshop_url)
    #context.driver.delete_all_cookies()


@when(u'Hit the tempory mail URL')
def tempMail(context):
    context.driver.get("https://temp-mail.org/en/")
    context.driver.maximize_window()

@when(u'Copy the mail')
def copyemailaddress(context):
    time.sleep(20)
    context.driver.find_element_by_id('click-to-copy').click()


@when(u'Open the new tab')
def newtab(context):
    context.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    context.driver.maximize_window()
    time.sleep(5)


@when(u'Hit the quantuvos URL')
def qURL(context):
    context.driver.execute_script("window.open('about:blank','secondtab');")
    context.driver.switch_to.window("secondtab")
    context.driver.get('https://platform-dev.quantuvos.com/login')

    #context.driver.execute_script("window.open('https://platform-dev.quantuvos.com/login');")
    context.driver.maximize_window()
    time.sleep(10)


@when(u'Enter "{email}" and "{password}" and click on submit')
def loginops(context,email,password):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_name("email").send_keys(email)
    context.driver.find_element_by_name("password").send_keys(password)
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(10)


@when(u'Onboard New client')
def sendwelcome(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()

    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("individual-client").click()

    time.sleep(10)
    context.driver.find_element_by_name("individualclientfirstname").send_keys("Qa")
    context.driver.find_element_by_name("individualclientlastname").send_keys("Test")
    context.driver.find_element_by_name("individualclientemail").send_keys(Keys.CONTROL, 'v')
    context.driver.find_element_by_name("individualclientallocationhour").send_keys("5")

    context.driver.find_element_by_id("btndisable").click()

    time.sleep(10)

    context.driver.switch_to.window(context.driver.window_handles[0])
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)
    context.driver.find_element_by_link_text("quantuvos@gmail.com").click()
    time.sleep(10)
    #context.driver.find_element_by_class_name('viewLink')
    #time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 800)")
    context.driver.find_element_by_link_text("Start").click()
    time.sleep(10)


    time.sleep(10)
    context.driver.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    context.driver.find_element_by_id('btnSubmit').click()
    time.sleep(10)

    context.driver.execute_script("window.open('about:blank','thirdtab');")
    context.driver.switch_to.window("thirdtab")
    context.driver.get('https://temp-mail.org/en/')
    context.driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(10)
    context.driver.find_element_by_link_text("Quantuvos Email Confirmation").click()
    time.sleep(10)
    context.driver.execute_script("window.scrollTo(0, 600)")
    context.driver.find_element_by_link_text("Confirm").click()
    time.sleep(10)

    time.sleep(10)
    time.sleep(20)

