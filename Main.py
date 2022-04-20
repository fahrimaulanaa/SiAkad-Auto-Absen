import time
import pytz
import scriptabsen as script
from selenium import webdriver
from datetime import datetime

print("Bot Absen SMK Telkom Malang")
print("==========================================================")
print("")

while True:
    time.sleep(5)
    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)

    if time_now.strftime("%H:%M") == '06:35':
        try:
            script.login()
        except:
            print("Error")
            continue

    