from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import xlsxwriter
import xlwt
from xlwt import Workbook


profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True


web = webdriver.Firefox(firefox_profile=profile)
url1 = "https://edu-devits5-applications.adaptit.com/"
web.get(url1)
web.maximize_window()
time.sleep(3)
# if web.find_element(By.XPATH, '/html/body/app-root/app-account/main/app-account-landing/div[2]/div').is_displayed():
#     worksheet.write(1, 0, 'Before we begin page')
#     worksheet.write(1, 1, 'SUCCESS')
#     workbook.save('Automation_Report.xls')
# else:
#     worksheet.write(1, 0, 'Before we begin page')
#     worksheet.write(1, 1, 'FAILED')
#     workbook.save('Automation_Report.xls')

student_num = web.find_element(By.XPATH, '//*[@id="mat-radio-3"]/label/span[1]')
student_num.click()
return_student = web.find_element(By.XPATH, '//*[@id="mat-radio-6"]/label/span[1]/span[1]')
return_student.click()
login = web.find_element(By.XPATH,
                         '/html/body/app-root/app-account/main/app-account-landing/div[2]/div/div/div[2]/div/div[1]/button[2]')
login.click()
google_login = web.find_element(By.XPATH,
                                '/html/body/app-root/app-account/main/app-account-landing/div[2]/div/div/div[2]/div/div[2]/span/app-sign-in/div/app-google-sign-in/div/button')
google_login.click()
windowsOpened = web.window_handles
time.sleep(3)

web.switch_to.window(windowsOpened[1])
email = 'maliviwediko03@gmail.com'
email_field = web.find_element(By.XPATH,
                               '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]')
email_field.send_keys(email)
time.sleep(3)
log_continue = web.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[1]')
log_continue.click()
time.sleep(2)

web.switch_to.window(web.window_handles[0])
time.sleep(2)

status.click()
time.sleep(2)
selection = web.find_element(By.XPATH, awaitSelectB_xpath)
selection.click()
time.sleep(5)
Select_Search = web.find_element(By.XPATH, qSearch_xpath)
web.execute_script("arguments[0].scrollIntoView();", Select_Search)
time.sleep(3)
header = web.find_element(By.XPATH,
                          '/html/body/app-root/app-dashboard/mat-sidenav-container/mat-sidenav-content/main/app-short-list/app-recent-applications-list/div/div[1]/div/img')
web.execute_script("arguments[0].scrollIntoView();", header)
time.sleep(3)
worksheet1.write(5, 0, 'Scrolling')
worksheet1.write(5, 1, 'SUCCESS')
workbook1.save('Selections_Status.xls')
try:
    AcademicYear = web.find_element(By.XPATH, qAcademicYear_xpath)
    AcademicYear.click()
    time.sleep(1)
    yearDropdown = WebDriverWait(web, 2).until(
        ec.visibility_of_element_located((By.XPATH, "//div[@title='2022']"))).click()
    yearDropdown.click()
    time.sleep(3)
    web.quit()
except:
    time.sleep(7)
    web.quit()
except:
    worksheet1.write(6, 0, 'Scrolling')
worksheet1.write(6, 1, 'FAILED')
workbook1.save('Selections_Status.xls')
time.sleep(7)
web.quit()