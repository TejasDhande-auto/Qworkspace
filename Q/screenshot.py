from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)
DNS = r'C:\Users\kanaka\Desktop SS.png'
driver.save_screenshot(DNS)
screenshot = Image.open(DNS)
screenshot.show()