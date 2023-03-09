from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv

username = 'maliviwediko03@gmail.com'
password = 'Diko0308%'




#Home screen
web = webdriver.Chrome()
url1 = "https://www.takealot.com/"
web.get(url1)
time.sleep(4)

#Login
login_B = web.find_element(By.XPATH, '//*[@id="shopfront-app"]/div[2]/div/div/div[2]/div/div[1]/ul/li[1]/a')
login_B.click()

search_B = web.find_element(By.XPATH, '//*[@id="shopfront-app"]/header/div/div/div[2]/form/div/div[1]/input')
search_B.send_keys(username)


username_textfill = web.find_element(By.XPATH, '//*[@id="customer_login_email"]')
username_textfill.send_keys(username)

username_textfill = web.find_element(By.XPATH, '//*[@id="customer_login_password"]')
username_textfill.send_keys(password)

recaptcha = web.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[4]')
recaptcha.click()

google_login = web.find_element(By.XPATH, '//*[@id="body"]/div[11]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/span[1]/button/div[2]')
google_login.click()

web.quit()