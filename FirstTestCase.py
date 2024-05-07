# Webdrive is a module that is available in selenium package .

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")

input_element.clear()   

input_element.send_keys("Abdul Rafay Atiq - Associate Software Engineer"+Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Abdul Rafay Atiq - Associate Software Engineer"))
)

print("Program to warr gaya")

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Abdul Rafay Atiq - Associate Software Engineer")
link.click()

time.sleep(10)
driver.quit()













