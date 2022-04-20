from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytz

# Set up the Chrome driver
chromes = webdriver.ChromeOptions()
chromes.add_argument('user-data-dir=D:\ChromeProfile')
driver = webdriver.Chrome(executable_path='D:\SiAkad Auto Absen\chromedriver.exe', chrome_options=chromes)

driver.get("https://siswa.smktelkom-mlg.sch.id/presnow")
time_now = datetime.now(pytz.timezone('Asia/Jakarta'))

#Click the absen button
if time_now.strftime('%H:%M') == '09:22':
    try:
        driver.refresh()
        time.sleep(0.1)
        inputabsen = driver.find_element_by_xpath('//label[@for="M"]')
        luring = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/div[2]/form/div/div[2]/div[2]/div[2]/label[2]')
        simpan = driver.find_element_by_id("simpan")
        inputabsen.click()
        time.sleep(0.4)
        luring.click()
        simpan.click()
        driver.switch_to.alert.accept()
    except:
        pass