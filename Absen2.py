from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import pytz

# Set up the Chrome driver
chromes = webdriver.ChromeOptions()
chromes.add_argument('user-data-dir=D:\ChromeProfile')
driver = webdriver.Chrome(executable_path='D:\SiAkad Auto Absen\chromedriver.exe', chrome_options=chromes)

driver.get("https://siswa.smktelkom-mlg.sch.id/presnow")
time_now = datetime.now(pytz.timezone('Asia/Jakarta'))

#Click the absen button
if time_now.strftime('%H:%M') == '06:50':
    try:
        driver.refresh()

        masuk = driver.find_element_by_xpath('//label[@for="M"]')
        masuk.click()

        daring = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), 'DARING')]")))
        daring.click()

        simpan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), 'SIMPAN')]")))
        simpan.click()
        
        alert = driver.switch_to.alert
        alert.accept()

    except:
        pass