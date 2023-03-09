from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

username = '********' # This is not my username, 
password = '*****' 

#Home screen
web = webdriver.Chrome()
url1 = "https://watvnewsong.org/home.wmc"
web.get(url1)
web.maximize_window()       #maximize window
time.sleep(3)

#login
login = web.find_element(By.XPATH, '//*[@id="request"]/div[1]/div[3]/div')
login.click()

watvid = web.find_element(By.XPATH, '//*[@id="id"]')
watvid.send_keys(username)
pass_w = web.find_element(By.XPATH, '//*[@id="password"]')
pass_w.send_keys(password)
login_b = web.find_element(By.XPATH, '//*[@id="btnLogin"]')
login_b.click()
time.sleep(3)
web.execute_script("window.scrollTo(0,document.body.scrollHeight)")         #scroll to bottom
time.sleep(2)

#events
events = web.find_element(By.XPATH, '//*[@id="request"]/div[2]/div[4]/div/div[1]/div/div[5]/div/a/img')
events.click()
time.sleep(7)
#selecting from dropdown
lang = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div[1]/div[1]/select')
select = Select(lang)
time.sleep(2)
select.select_by_visible_text('Korean')
time.sleep(5)

#playall
playlist1 = web.find_element(By.XPATH, '//*[@id="request"]/div[2]/div[1]/div/div[2]/a[2]')
playlist1.click()
time.sleep(3)
#accept the popup
web.switch_to.alert.accept()
time.sleep(5000)

logout = web.find_element(By.XPATH, '//*[@id="request"]/div[1]/div[3]/div/a')
logout.click()