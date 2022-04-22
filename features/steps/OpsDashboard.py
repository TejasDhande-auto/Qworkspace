import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from features import myglobal as gb, environment
from selenium.webdriver.support.ui import Select

@when(u'Enter Ops credentials "opsqdev@outlook.com" and "Kanaka@123"')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_name("email").send_keys("opsqdev2021@outlook.com")
    context.driver.find_element_by_name("password").send_keys("Quantuvos@123")
    context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(5)


@then(u'Operation dashboard should display')
def step_impl(context):
    text1 = context.driver.find_element_by_xpath("//span[text()=' Operations Dashboard ']").text
    if text1 == "Operations Dashboard":
        allure.attach("",name="Operation dashboard is opened")
    else:
        raise Exception("Operation dashboard is mot opem")


@given(u'Sessions screen should be open')
def step_impl(context):
    text2 = context.driver.find_element_by_xpath("//h4[text()='Sessions ']").text
    if text2 == "Sessions":
        allure.attach("",name="Sessions screen is open")

    else:
        raise Exception("Sessions screen is not default selected")

@when(u'Select session')
def step_impl(context):
    time.sleep(3)
    allure.attach("",name="Selecting session one bye one")

@then(u'Related buttons should enable')
def step_impl(context):
    status = ("Scheduled", "Rescheduled", "Rescheduling", "Follow Up", "Cancelled", "Completed")
    for i in range(6):

        time.sleep(5)
        context.driver.find_element_by_xpath('(//span[@class="ag-icon ag-icon-menu"])[2]').click()
        time.sleep(1)
        context.driver.find_element_by_xpath('(//input[@placeholder="Filter..."])[1]').clear()
        context.driver.find_element_by_xpath('(//input[@placeholder="Filter..."])[1]').send_keys(status[i])
        time.sleep(2)
        context.driver.find_element_by_xpath('(//div[@aria-colindex="1"])[2]').click()
        time.sleep(1)
        Current_status = status[i]
        print(Current_status)
        if context.driver.find_element_by_xpath("//button[text()='View']").is_enabled() and context.driver.find_element_by_xpath(
                "//button[text()='Edit']").is_enabled() and context.driver.find_element_by_xpath(
            "//button[text()='Reschedule']").is_enabled() and Current_status == "Scheduled" or Current_status == "Rescheduling" or Current_status == "Follow Up":

            allure.attach("All three buttons are enabled",name=status[i], attachment_type=AttachmentType.TEXT)
            print("Looks good for", status[i])

        elif context.driver.find_element_by_xpath("//button[text()='View']").is_enabled() and context.driver.find_element_by_xpath(
                "//button[text()='Edit']").is_enabled() and Current_status == "Rescheduled":

            allure.attach("View and Edit buttons are enabled",name=status[i], attachment_type=AttachmentType.TEXT)

        elif context.driver.find_element_by_xpath(
                "//button[text()='View']").is_enabled() and Current_status == "Completed" or Current_status == "Cancelled":

            allure.attach("View button is enabled",name=status[i], attachment_type=AttachmentType.TEXT)

        else:
            raise Exception


@when(u'Click on dropdown and select next 10 days')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select').click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[2]').click()
    time.sleep(5)


@then(u'Sessions in next 10 days should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Next 10 Days", attachment_type=AttachmentType.PNG)


@when(u'Click on dropdown and select next 20 days')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[3]').click()
    time.sleep(5)


@then(u'Sessions in next 20 days should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Next 20 Days", attachment_type=AttachmentType.PNG)


@when(u'Click on dropdown and select next 30 days')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[4]').click()
    time.sleep(5) 


@then(u'Sessions in next 30 days should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Next 30 Days", attachment_type=AttachmentType.PNG)


@when(u'Click on dropdown and select All option')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="row-Operations-head"]/div/div[2]/select/option[1]').click()
    time.sleep(5)


@then(u'All Sessions details should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="All day sessions", attachment_type=AttachmentType.PNG)


@when(u'Type "Scheduled" in search box')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Scheduled")
    time.sleep(2)


@then(u'Matched results should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Scheduled Session", attachment_type=AttachmentType.PNG)


@when(u'select one session and click on view')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-operations-dashboard/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='View']").click()
    time.sleep(5)


@then(u'Session detail should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Session Details", attachment_type=AttachmentType.PNG)
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Close']").click()
    time.sleep(2)


@when(u'select one session and click on edit')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Edit']").click()
    time.sleep(2)


@when(u'Edit the session status and reason')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath(("//select[@name='status']")).click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//option[@value='Rescheduling']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(("//select[@name='reason']")).click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//option[text()='Qerror']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//*[@id="uBody"]/modal-container/div/div/form/div[2]/textarea').send_keys(
        "Automate change")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(5)


@then(u'Selected session should get updated')
def step_impl(context):
    try:
        toastmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if toastmsg == "Session have been updated":
            print(toastmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Session have been updated")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        time.sleep(2)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Session Updated", attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        raise Exception("Unable to update session")


@when(u'Click on Customers')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//a[@title='Customers']").click()
    time.sleep(5)


@then(u'Customers screen should get opened')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Customer screen", attachment_type=AttachmentType.PNG)


@when(u'Click on Add, enter customer details and click on submit')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[text()='Add']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@name='customerName']").send_keys("Automatecustomer")
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@name='PointOfContact']").send_keys("Seleniumcustomer")
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@name='ContactNo']").send_keys("9876543210")
    time.sleep(5)
    context.driver.find_element_by_name("Email").send_keys("automate@customer.com")
    time.sleep(5)
    context.driver.find_element_by_xpath("//select[@value='Active']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//option[text()=' Active']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(5)


@then(u'Customers should get added to platform')
def step_impl(context):

    custadd = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    if custadd == "Email address has been previously used":
        allure.attach("",name="Email address has been previously used")
        time.sleep(2)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        context.driver.find_element_by_xpath("(//button[text()='Cancel'])[1]").click()

    elif custadd == "Customer name has been previously used.":
        allure.attach("",name="Customer name has been previously used.")
        time.sleep(2)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        context.driver.find_element_by_xpath("(//button[text()='Cancel'])[1]").click()

    else:
        allure.attach("",name="New customer has been added successfully")
        allure.attach(context.driver.get_screenshot_as_png(), name="Customer Added",
                      attachment_type=AttachmentType.PNG)
        time.sleep(2)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
        time.sleep(3)
        context.driver.find_element_by_xpath(
            "/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
            "AutomateCustomer")
        time.sleep(5)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()


@when(u'Click on Edit, edit details and click on submit')
def step_impl(context):
    allure.attach("",name="Yet to be define")
    # time.sleep(2)
    # context.driver.find_element_by_xpath(
    #     '/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input').click()
    # time.sleep(2)
    # context.driver.find_element_by_xpath("//button[text()='Edit']").click()
    # time.sleep(5)
    # context.driver.find_element_by_xpath('(//input[@name="PointOfContact"])[2]').clear()
    # context.driver.find_element_by_xpath("(//input[@name='PointOfContact'])[2]").send_keys("Seleniumcustomer")
    # time.sleep(2)
    # context.driver.execute_script("window.scrollTo(0, 500)")
    # time.sleep(2)
    # context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    # time.sleep(2)
    # context.driver.find_element_by_xpath(
    #     '/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input').click()
    # time.sleep(2)
    #

@then(u'Customer details should get updated in platform')
def step_impl(context):
    allure.attach("", name="Yet to be define")

@when(u'Click on filter and apply filter')
def step_impl(context):
    context.driver.find_element_by_xpath('//img[@alt="filter icon"]').click()
    time.sleep(2)
    drp1 = Select(context.driver.find_element_by_xpath('//select[@formcontrolname="colname"]'))
    drp1.select_by_value("b_customerName")
    time.sleep(2)
    drp2 = Select(context.driver.find_element_by_xpath('//select[@formcontrolname="filterType"]'))
    drp2.select_by_value("iexact")
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@formcontrolname="searchKey"]').send_keys("Kanaka cons pune")
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Apply']").click()
    time.sleep(2)
  


@then(u'Matched customers should display on screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Customer Filter", attachment_type=AttachmentType.PNG)


@when(u'Select one of customer and click on View')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath(
        '/html/body/app-root/app-customers/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input').click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='View']").click()


@then(u'Customer specific client should display on clients screen')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Customer Filter", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    context.driver.back()
    time.sleep(5)


@given(u'Send Welcome screen should be open and Individual client should be selected')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//*[@id="opt-onboardingid"]').click()
    time.sleep(8)
    context.driver.find_element_by_xpath('//*[@id="opt-Welcomeid"]').click()
    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("individual-client").click()


@when(u'Enter individual-client details and click on submit')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_name("individualclientfirstname").send_keys("IndividualAutomate")
    context.driver.find_element_by_name("individualclientlastname").send_keys("Client")
    context.driver.find_element_by_name("individualclientemail").send_keys("ffsfjhf@sjhffkh.com")
    context.driver.find_element_by_name("individualclientallocationhour").send_keys("55")
    time.sleep(5)
    context.driver.find_element_by_id("btndisable").click()
    time.sleep(5)


@then(u'Appropriate message should display (Individual client)')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "Existing User":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Existing User")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach("",name="Email invitation has been to the individual client")
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        time.sleep(2)

    except:
         allure.attach(context.driver.get_screenshot_as_png(), name="Individual client", attachment_type=AttachmentType.PNG)
         raise Exception("Error in Email invitation")


@when(u'Upload individual.csv file and click on Submit')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@id="file"]').send_keys(
        "C://Users//kanaka//Downloads//CSV//Individual_Client.csv")
    time.sleep(3)
    context.driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
    time.sleep(5)


@then(u'Appropriate message should display (Bulk Individual clients)')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Individual client bulk", attachment_type=AttachmentType.PNG)
    try:
        context.driver.find_element_by_xpath("//button[text()=' OK ']").click()
        time.sleep(2)
    except:
        allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Toast message",attachment_type=AttachmentType.TEXT)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        pass


@given(u'Send Welcome screen should be open and customer client should be selected')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(10)
    context.driver.find_element_by_id("clienttype").click()


@when(u'Enter customer-client details and click on submit')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_name("customerclientfirstname").send_keys("CustomerAutomate")
    context.driver.find_element_by_name("customerclientlastname").send_keys("Client")
    context.driver.find_element_by_name("customerclientemail").send_keys("gfhsgj@shh.in")
    context.driver.find_element_by_name("customerclientallocationhour").send_keys("65")
    context.driver.find_element_by_name("customerclientcompanyid").send_keys("Kanaka")
    time.sleep(5)
    context.driver.find_element_by_id("btnsubmit").click()
    time.sleep(3)


@then(u'Appropriate message should display (Customer client)')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "Existing User":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Existing User")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach("", name="Email invitation has been to the Customer client")
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        time.sleep(2)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Individual client",
                      attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        raise Exception("Error in Email invitation")



@when(u'Upload customerclient.csv file and click on Submit')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@id="file"]').send_keys(
        "C://Users//kanaka//Downloads//CSV//Customer_Client.csv")
    time.sleep(3)
    context.driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
    time.sleep(5)


@then(u'Appropriate message should display (Bulk Customer clients)')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Customer client", attachment_type=AttachmentType.PNG)
    try:
        context.driver.find_element_by_xpath("//button[text()=' OK ']").click()
        time.sleep(2)
    except:
        allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Toast message",attachment_type=AttachmentType.TEXT)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        pass


@given(u'Send Welcome screen should be open and Coach should be selected')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_id("dropdownMenuLink").click()
    time.sleep(3)
    context.driver.find_element_by_id("coachtype").click()
    time.sleep(5)


@when(u'Enter Coach details and click on submit')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_name("coachfirstname").send_keys("CoachABC")
    context.driver.find_element_by_name("coachlastname").send_keys("XYZ")
    context.driver.find_element_by_name("coachemail").send_keys("Customer@automatecoach.in")
    time.sleep(5)
    context.driver.find_element_by_id("coachbtn").click()
    time.sleep(10)


@then(u'Appropriate message should display (Coach)')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "Existing User":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Existing User")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach("", name="Email invitation has been to the coach")
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        time.sleep(2)

    except:
        allure.attach(context.driver.get_screenshot_as_png(), name="Coach",
                      attachment_type=AttachmentType.PNG)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        raise Exception("Error in Email invitation")


@when(u'Upload Coach.csv file and click on Submit')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@id="file"]').send_keys("C://Users//kanaka//Downloads//CSV//Coach.csv")
    time.sleep(3)
    context.driver.find_element_by_xpath("(//button[text()=' Submit '])[2]").click()
    time.sleep(5)


@then(u'Appropriate message should display (Bulk Coach)')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach bulk ", attachment_type=AttachmentType.PNG)
    try:
        context.driver.find_element_by_xpath("//button[text()=' OK ']").click()
        time.sleep(2)
    except:
        allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,name="Toast message",attachment_type=AttachmentType.TEXT)
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        pass


@when(u'Click on Onboarding-Clients screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Clients'])[1]").click()
    time.sleep(5)


@then(u'Onboarding-Clients screen should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Onboarding-Clients ", attachment_type=AttachmentType.PNG)


@when(u'Click on Onboarding-Coaches screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Coaches'])[1]").click()
    time.sleep(5)


@then(u'Onboarding-Coaches screen should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Onboarding-Coaches ",
                  attachment_type=AttachmentType.PNG)


@when(u'Click on Onboarding-Coach selection screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Coach Selection'])[1]").click()
    time.sleep(5)


@then(u'Onboarding-Coach selection screen should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach selection screen",
                  attachment_type=AttachmentType.PNG)

    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()=' - Onboarding']").click()
    time.sleep(2)

@when(u'Click on Coaches on ops dashboard screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Coaches'])[2]").click()
    time.sleep(10)


@then(u'Coaches screen on ops dashboard should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Coached",
                  attachment_type=AttachmentType.PNG)


@when(u'Select one coach and click on edit')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Coaches'])[2]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
        "QCoach1")
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-coach/div/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Edit']").click()
    time.sleep(5)


@when(u'Edit the details of Coaches')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@name="data[LastName]"]').clear()
    context.driver.find_element_by_xpath('//input[@name="data[LastName]"]').send_keys("Automatelastname")
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(2)
    context.driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
    time.sleep(5)

@then(u'Coach details should get updated by ops user')

def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach detail update",
                  attachment_type=AttachmentType.PNG)
    
    context.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach detail update",
                  attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
    context.driver.find_element_by_xpath("//a[text()=' Back']").click()
    time.sleep(5)


@when(u'Click Add button on Coaches screen')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[text()='Add']").click()
    time.sleep(5)



@then(u'Coach invitation screen should be open')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach Invitation screen",
                  attachment_type=AttachmentType.PNG)
    context.driver.back()
    time.sleep(5)


@when(u'Click on Clients on ops dashboard screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[text()='Clients'])[2]").click()
    time.sleep(30)

@then(u'Clients screen on ops dashboard should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Clients",
                  attachment_type=AttachmentType.PNG)

@when(u'Select one client and click on edit')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[3]/div/div/div/div/div[2]/div/div[2]/input").send_keys(
        "Qtestclient1")
    time.sleep(3)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-clients/div[1]/div/div[2]/div/div[2]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Edit']").click()
    time.sleep(5)


@when(u'Edit the details of client')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath('//input[@name="data[LastName]"]').clear()
    context.driver.find_element_by_xpath('//input[@name="data[LastName]"]').send_keys("Automatelastname")
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(2)
    context.driver.find_element_by_xpath('//button[@name="data[submit]"]').click()
    time.sleep(5)


@then(u'Client details should get updated by ops user')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Client update",
                  attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Coach detail update",
                  attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

    context.driver.find_element_by_xpath("//a[text()=' Back']").click()
    time.sleep(5)


@when(u'Click Add button on clients screen')
def step_impl(context):
    time.sleep(25)
    context.driver.find_element_by_xpath("//button[text()='Add']").click()
    time.sleep(5)


@then(u'Individual client invitation screen should be open')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Client Invitation screen",
                  attachment_type=AttachmentType.PNG)
    time.sleep(5)
    context.driver.back()
    time.sleep(5)

@when(u'Click on Ops-Network Q Resources')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()=' + Network Q']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Resources']").click()
    time.sleep(5)


@then(u'Ops-Network Q Resources screen should be open')
def step_impl(context):
    if context.driver.find_element_by_xpath("//span[text()=' Resources ']").is_displayed():
        print("Network Q screen is displayed")
        allure.attach("", name="Network Q screen is displayed")
    else:
        allure.attach("", name="Error : Network Q screen is not displayed")
        raise Exception("Error : Network Q screen is not displayed")

@when(u'Click on Tabs on Ops-Network Q Resources')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//a[text()='Webinars']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Webinars", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Activity']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Activity", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Podcasts']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Podcasts", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Ted Talk']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Ted Talk", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Article']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Article", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Tips']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Tips", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Assessment']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Assessment", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Videos']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Videos", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        context.driver.find_element_by_xpath("//a[text()='Book']").click()
        time.sleep(3)
        allure.attach(context.driver.get_screenshot_as_png(), name="Book", attachment_type=AttachmentType.PNG)
        time.sleep(3)
    except:
        raise Exception("Tabs missing")

    context.driver.find_element_by_xpath("//a[text()='Home']").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Home", attachment_type=AttachmentType.PNG)
    time.sleep(3)


@then(u'Tab related resources should display to Ops on screen')
def step_impl(context):
    print("Yes opened successfully")
    allure.attach("", name="Screenshots has been attached")

@when(u'Enter text in search box on Ops-Network Q Resources screen')
def step_impl(context):
    
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@id='myInput']").send_keys("Prepar")
    time.sleep(2)

@then(u'Matched resources should display to Ops')
def step_impl(context):
    context.driver.find_element_by_xpath("(//div[@id='run'])[1]").click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.find_element_by_xpath("//button[text()='Close']").click()
    time.sleep(2)


@when(u'Enter text in advanced search box on Ops-Network Q Resources screen')
def step_impl(context):
    context.driver.find_element_by_xpath('//button[@title="Advanced Search"]').click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@name='titileSearchValue']").send_keys("Prepar")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='descriptionSearchValue']").send_keys("Prepare")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='authorSearchValue']").send_keys("Steve")
    time.sleep(1)
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault1']").click()  # And1
    context.driver.find_element_by_xpath("//*[@id='flexRadioDefault3']").click()  # and2
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Apply']").click()
    time.sleep(3)


@then(u'Matched resources to advanced search should display on Ops-Network Q')
def step_impl(context):
    
    if "Preparing for your first Coaching Session" == context.driver.find_element_by_xpath(
            "//span[text()=' Preparing for your first Coaching Session ']").text:
        print("Advanced search is successfull")
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("",name="Matched resources displayed")
    else:
        context.driver.find_element_by_xpath(
            '//*[@id="WelcometoNetworkQ"]/div/div[2]/div/div/div[1]/div/div[2]/div/div/img').click()
        print("Filter Resets")
        allure.attach("",name="Filter has been reset")


@given(u'Submit Resource modal window should be open on Ops-Network Q Resources screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='SUBMIT NEW RESOURCE']").click()
    time.sleep(2)


@when(u'Enter the resource details and click on save Ops-Network Q Resources screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath('//input[@id="Title"]').send_keys("uhs")

    context.driver.find_element_by_xpath('//textarea[@id="Description"]').send_keys("fsffsfsf")
    context.driver.find_element_by_xpath('//input[@id="Author"]').send_keys("sfsfsfs")
    time.sleep(2)
    context.driver.execute_script("arguments[0].scrollIntoView();",
                                  context.driver.find_element_by_xpath("//label[text()='Resource for coach']"))
    time.sleep(5)
    context.driver.find_element_by_xpath('//select[@id="Type"]').click()
    context.driver.find_element_by_xpath("//option[text()='Tips']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath('//select[@id="Category"]').click()
    context.driver.find_element_by_xpath("//option[text()='Diversity, Equity and Inclusion']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//input[@id="URL"]').send_keys("www.itssuotmation.things")
    time.sleep(1)
    context.driver.find_element_by_xpath('//input[@id="DurationTime"]').send_keys("15")
    time.sleep(1)
    context.driver.find_element_by_xpath("//span[text()='Save']").click()


@then(u'Resource created by ops user should be submitted for approval')
def step_impl(context):
    time.sleep(3)
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "resource URL already exist":
            context.driver.find_element_by_xpath("//span[text()='Cancel']").click()
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="resource URL already exist")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        elif errmsg == "Resources has been submitted for approval":
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Resource has been submitted for approval")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        else:
            allure.attach(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text,
                          name="Diffrent error msg", attachment_type=AttachmentType.TEXT)
            print(context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text)
            context.driver.find_element_by_xpath("//span[text()='Cancel']").click()
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        time.sleep(2)

    except:
        context.driver.find_element_by_xpath("//span[text()='Cancel']").click()
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        raise Exception("Unable to submit resource")



@when(u'Click on Resources Approval')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Resources Approval']").click()
    time.sleep(5)


@then(u'Resources approval screen should display')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Resources Approval", attachment_type=AttachmentType.PNG)


@when(u'Select on resource and edit the resource details')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-resources-approval/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()=' Edit ']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath('//textarea[@id="Description"]').send_keys("  extra description added by automation")
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Save']").click()
    time.sleep(5)
  


@then(u'Resouce details should be updated')
def step_impl(context):
    errmsg1 = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    print(errmsg1)
    if errmsg1 == "Resource details has been updated":
        print(errmsg1)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Resource detail has been updated")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

    else:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Resource has been submitted for approval")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

        try:
            context.driver.find_element_by_xpath('//button[@aria-label="Close"]').click()
        except:
            pass


@when(u'Select one of resource and click on approve')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "/html/body/app-root/app-resources-approval/div[1]/div/div[2]/div/div[1]/ag-grid-angular/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/input").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Approve']").click()
    time.sleep(5)

@then(u'Resource should be approved')
def step_impl(context):
    time.sleep(2)
    resourceapprove = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
    print(resourceapprove)
    if resourceapprove == "Selected resource(s) approved":
        print(resourceapprove)
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Resource detail has been updated")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()

    else:
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach("", name="Resource has been submitted for approval")
        context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        context.driver.find_element_by_xpath('//button[@aria-label="Close"]').click()

    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()=' - Network Q']").click()
    time.sleep(2)

@when(u'Click on Ops-Settings')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath("//span[text()=' Settings']").click()
    time.sleep(2)


@then(u'Ops-Settings screen should displayed')
def step_impl(context):
    allure.attach(context.driver.get_screenshot_as_png(), name="Settings", attachment_type=AttachmentType.PNG)


@when(u'Click on change password icon on ops-settings screen')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//img[@title='Change Password']").click()
    time.sleep(3)


@when(u'Enter Incorrect old password and New password of ops and click on Submit')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_name("oldPassword").send_keys("Kanaka@123")
    context.driver.find_element_by_name("newPassword").send_keys("Qwerty@123")
    context.driver.find_element_by_name("confirmPassword").send_keys("Qwerty@123")
    time.sleep(3)
    context.driver.find_element_by_xpath("//button[text()='Submit']").click()
    time.sleep(2)
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(2)
    context.driver.find_element_by_xpath("(//button[text()='Close'])[2]").click()
    time.sleep(3)


@then(u'Appropriate error message should display on ops-settings screen')
def step_impl(context):
    try:
        errmsg = context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').text
        if errmsg == "old password is incorrect..":
            print(errmsg)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="old password is incorrect : Expected")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        else:
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach("", name="Password changed successfully")
            context.driver.find_element_by_xpath('//*[@id="toast-container"]/div').click()
        time.sleep(2)

    except:
        raise Exception("Not a proper toaster")




@when(u'Click Logout on ops dashboard')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//span[text()='Logout']").click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)


@then(u'Login page should be displayed')
def step_impl(context):
    time.sleep(2)
    if context.driver.find_element_by_xpath('//*[@id="btnSubmit"]').is_displayed():
        allure.attach("", "User logged out successfully")

    else:
        raise Exception("Logout Functionality breaks")



