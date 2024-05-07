from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path="C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"  # as it is giving productprice[0] or [1] etc..
product_prefix = "product"


# Handling the cookies consent banner as they appear as noti to take the consent from the user
try:
    cookie_consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cc_btn_accept_all"))
    )
    cookie_consent_button.click()


except:
    pass

# //* selects all the elements in the doc, irrespective of their name
# [contains(text() , 'English')] filters elements based on text , here is "English".

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH , "//*[contains(text() , 'English')]" ))
)

language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)


cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",",""))

    # print(cookies_count)
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",","")

        if not product_price.isdigit():
            continue
        
        product_price = int(product_price.replace(",",""))


        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
