import time
from datetime import date, timedelta

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get("https://temp-mail.org/en/")
time.sleep(20)
text = driver.find_element_by_id("mail").getText()
print(text)