import time
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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def getInstVeriCode(mailName, domain, driver):

    INST_CODE = 'https://email-fake.com/' + domain + '/' + mailName
    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)
    
    # button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/a/button").click()
    # time.sleep(3)
    t = driver.title

    while True:
        if t[:4]=="Fake":
            driver.refresh()
            t = driver.title
            print(t)
            time.sleep(1)
        else:
            break

    # code = browser.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
    # code = code.replace("is your Instagram code", "")
    code = t[:6]
    driver.switch_to.window(driver.window_handles[0])
    return code

print(getInstVeriCode('lgoce99','agentsa.shop',driver))