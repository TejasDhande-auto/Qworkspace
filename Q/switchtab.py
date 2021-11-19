from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')

driver.execute_script("window.open('');")
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://facebook.com")
time.sleep(5)

driver.close()
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.yahoo.com")
time.sleep(5)

#driver.close()