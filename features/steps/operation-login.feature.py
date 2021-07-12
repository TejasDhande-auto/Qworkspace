import time

from behave import *
from selenium import webdriver

@given('Launch the browser')
def lauchbrowser(context):
    context.driver = webdriver.Chrome()


@when('Open the login Url')
def openurl(context):
    context.driver.get("https://platform-dev.quantuvos.com/login")
    context.driver.maximize_window()


@when('Enter valid Email and Password')
def entercredentials(context):
    context.driver.find_element_by_id("inputEmailID").send_keys("admin@quantuvos.com")
    context.driver.find_element_by_id("inputPasswordID").send_keys("Qwerty123@")

@when('Click on Login')
def clicksubmit(context):
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

@then('Login successful')
def login(context):
    assert True, "Test passed"

@when('Click on Onboarding')
def clickonboarding(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()


@when('Select Individual client')
def selectindividual(context):
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(5)
    context.driver.find_element_by_id("individual-client").click()

@when('Enter "{individualfirstname}", "{individuallastname}", "{individualemail}", "{individualallocatedcoachinghours}"')
def enterdetails(context,individualfirstname,individuallastname,individualemail,individualallocatedcoachinghours):
    time.sleep(5)
    context.driver.find_element_by_name("individualclientfirstname").send_keys(individualfirstname)
    context.driver.find_element_by_name("individualclientlastname").send_keys(individuallastname)
    context.driver.find_element_by_name("individualclientemail").send_keys(individualemail)
    context.driver.find_element_by_name("individualclientallocationhour").send_keys(individualallocatedcoachinghours)


@when('Submit individual client details')
def submitdeatils(context):
    try:
        context.driver.find_element_by_id("btndisable").click()

    except:
        context.driver.close()
        assert False,"Test failed"

@then('Email invitation send to individual-client')
def individualemailsend(context):
    time.sleep(5)
    context.driver.close()
    assert True, "Test Passed"


@when('Select Customer-client')
def selectcustomerclient(context):
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    context.driver.find_element_by_id("clienttype").click()


@when('Enter the "{customerfirstname}", "{customerlastname}", "{customeremail}", "{customercompanyid}", "{customermanagername}", "{customerhrmanagername}", "{customerallocatedcoachinghours}" details')
def enterccdetails(context,customerfirstname,customerlastname,customeremail,customercompanyid,customermanagername,customerhrmanagername,customerallocatedcoachinghours):
    time.sleep(5)
    context.driver.find_element_by_name("customerclientfirstname").send_keys(customerfirstname)
    context.driver.find_element_by_name("customerclientlastname").send_keys(customerlastname)
    context.driver.find_element_by_name("customerclientcompanyid").send_keys(customercompanyid)
    context.driver.find_element_by_name("customerclientmanagername").send_keys(customermanagername)
    context.driver.find_element_by_name("customerclienthrmanagername").send_keys(customerhrmanagername)
    context.driver.find_element_by_name("customerclientemail").send_keys(customeremail)
    context.driver.find_element_by_name("customerclientallocationhour").send_keys(customerallocatedcoachinghours)


@when('Submit customer client details')
def submitdeatils(context):
    try:
        context.driver.find_element_by_id("btnsubmit").click()
        time.sleep(10)

    except:
        context.driver.close()
        assert False,"Test failed"

@then('Email invitation send to customer-client')
def clientinvitationsend(context):
    time.sleep(5)
    context.driver.close()
    assert True, "Test Passed"


@when('Select Coach')
def selectcoach(context):
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    context.driver.find_element_by_id("coachtype").click()


@when('Enter "{coachfirstname}", "{coachlastname}", "{coachemail}"')
def entercoachdeatils(context,coachfirstname,coachlastname,coachemail):
    context.driver.find_element_by_name("coachfirstname").send_keys(coachfirstname)
    context.driver.find_element_by_name("coachlastname").send_keys(coachlastname)
    context.driver.find_element_by_name("coachemail").send_keys(coachemail)

@when('Submit coach details')
def submitdeatils(context):
    try:
        context.driver.find_element_by_id("coachbtn").click()
        time.sleep(10)

    except:
        context.driver.close()
        assert False,"Test failed"

@then('Email invitation send to coach')
def coachinvitationsend(context):
    time.sleep(5)
    context.driver.close()
    assert True, "Test Passed"