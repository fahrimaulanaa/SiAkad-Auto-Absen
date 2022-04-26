from psycopg2 import Time
import py
import filewriter
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import pytz

# Set up the Chrome driver
chromes = webdriver.ChromeOptions()
chromes.add_argument('user-data-dir=D:\ChromeProfile')
chromes.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe', chrome_options=chromes)

driver.get("https://siswa.smktelkom-mlg.sch.id/presnow")
WIB = pytz.timezone('Asia/Jakarta')
time_now = datetime.now(WIB)

while True:
    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)
    print("<----Menunggu pukul 06:00 WIB---->")

    if time_now.strftime('%H') == '06' and time_now.strftime('%M') == '00':
        try:
            driver.refresh()
            masuk = driver.find_element_by_xpath('//label[@for="M"]')
            masuk.click()

            daring = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), 'DARING')]")))
            daring.click()

            simpan = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), 'SIMPAN')]")))
            simpan.click()
        
            alert = driver.switch_to.alert
            alert.accept()

            #Check absen
            temp = driver.find_element_by_css_selector("div[class=number]")
            if(temp.text == 'Masuk'):
                print("--- Absen Success ---")

            print("ABSEN BERHASIL PADA ", time_now.strftime('%H:%M'), "WIB")
        except:
            print("ABSEN GAGAL PADA ", time_now.strftime('%H:%M'), "WIB") 
            pass
        driver.close()
        break




def cek_absen(browser):
    print("# Check Absen")
    tmp = browser.find_element_by_css_selector("div[class=number]")
    if(tmp.text == 'Masuk'):
        print("--- Absen Success ---")
        return True
    else:
        print("--- Absen Failed ---")
        return False
