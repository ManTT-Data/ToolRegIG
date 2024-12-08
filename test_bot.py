from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

acc = open("accounts.txt", "a")

# Initialize the parser
parser = argparse.ArgumentParser(description="Bot Account")

args = parser.parse_args()
ua = UserAgent()
try:
    userAgent = ua.random
except:
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
print(userAgent)

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.instagram.com/accounts/emailsignup/")
except Exception as e:
    print(f"Lỗi khi khởi tạo trình duyệt: {e}")

time.sleep(2)
try:
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))
    ).click()
except:
    pass

name = account.username()

# Fill the email value
email_field = driver.find_element(By.NAME, 'emailOrPhone')
fake_email = email.getFakeMail()[0]
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element(By.NAME, 'fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())

# Fill username value
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys(name)
print(name)

# Fill password value
password_field = driver.find_element(By.NAME, 'password')
acc_password = account.generatePassword()
password_field.send_keys(acc_password)

print(name + ":" + acc_password, file=acc)

acc.close()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign up')]"))).click()

time.sleep(5)

# Handle Birthday verification
try:
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@title='Month:']"))
    )
    Select(month_dropdown).select_by_visible_text("January")  # Hoặc chọn giá trị bạn muốn

    # Chọn Day
    day_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@title='Day:']"))
    )
    Select(day_dropdown).select_by_visible_text("1")  # Hoặc chọn giá trị bạn muốn

    # Chọn Year
    year_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@title='Year:']"))
    )
    Select(year_dropdown).select_by_visible_text("2000")  # Hoặc chọn giá trị bạn muốn

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
    )
    next_button.click()    
    time.sleep(5)
except Exception as e:
    print(f"Lỗi khi chọn ngày sinh: {e}")

time.sleep(5)

fMail = fake_email.split("@")
print(fMail)
mailName = fMail[0]
domain = fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
driver.find_element(By.NAME, 'email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(3)

#accepting the notifications.
next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
    )
next_button.click()    
time.sleep(20)

# #logout
# driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()

# # Logout: Nhấn vào nút đăng xuất
# driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()
driver.quit()
