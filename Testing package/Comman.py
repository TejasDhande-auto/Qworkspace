import time
from behave import *
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from datetime import date, timedelta

class First:
    def InvokeBrowser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = uc.Chrome(options=options)
        time.sleep(5)
        self.driver.get("https://platform-dev.quantuvos.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def InvokeLoginpage(self):

        self.driver.get("https://platform-dev.quantuvos.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("email").send_keys("qclientprofile@gmail.com")
        self.driver.find_element_by_name("password").send_keys("1234Test.")
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        time.sleep(10)

class TestStealth():
    def setup_method(self):
        print("setup_method")
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
       self.driver.quit()

    def test_stealth(self):
       print("Testing")
       self.driver.get("https://stealthxio.myshopify.com/products/stealthxio-practice")
       self.driver.set_window_size(968, 1039)
