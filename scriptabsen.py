from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytz

# Set up the Chrome driver
def browser():
    chromes = webdriver.ChromeOptions()
    chromes.add_argument('user-data-dir=D:\ChromeProfile')
    chromes.add_argument('--disable-notifications')
    chromes.add_argument('--disable-infobars')
    chromes.add_argument('--disable-extensions')    
    browser = webdriver.Chrome(executable_path='D:\chromedriver.exe', chrome_options=chromes)

    return browser


# Login to the website
def login(browser):
    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/welcome")
    except:
        browser.close();
        return False

    time.sleep(1)

    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")
    except:
        browser.close();
        return False

    while True:
        time_now = datetime.now(pytz.timezone('Asia/Jakarta'))
        if time_now.strftime('%H:%M') == '06:36':
           return absen(browser)

#Definition absen
def absen(browser):
    try:
        browser.refresh()
        inputabsen = browser.find_element_by_id("M")
        luring = browser.find_element_by_id("luring")
        simpan = browser.find_element_by_id("simpan")
        inputabsen.click()
        luring.click()
        simpan.click()
    except:
        pass

    return True