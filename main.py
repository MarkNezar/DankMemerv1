import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os, shutil

driver = webdriver.Chrome()

driver.get("https://discord.com/login")
print(">Opening Discord Login page...")
time.sleep(10)

#--------------- Edit Here -------------------------------------------------------------

# Enter your account details here 
username = ''
password = ''

# Copy the URL of channel where you wanna send messages and paste below
channelURL = ""

#-------------- Edit End ----------------------------------------------------------------

# Initialize and input email
username_input = driver.find_element_by_name('email')
username_input.send_keys(username)

# Initialize and input password
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

# Initialize and login
print(">Logging in...")
time.sleep(5)
login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div/div[2]/button[2]')
login_button.click()
print(">>Login Complete!")
print(">>Waiting to load")
time.sleep(10)

print(">Opening The Server Link...")
driver.get(channelURL)
time.sleep(5)

# actions
beg_count = 0
beg_cooldown = 45
beg_current=0

dig_count = 0
dig_cooldown = 40
dig_current=0

hunt_count = 0
hunt_cooldown = 40
hunt_current=0

fish_count = 0
fish_cooldown = 40
fish_current=0

dep_count = 0
dep_cooldown = 180
dep_current=0

# Msg Sending
msg_input = driver.find_element_by_xpath("//div[@id='app-mount']/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]")

while(1):
    time.sleep(1)

    if(beg_current <= 0):
        print("Begging for the {0} time".format(beg_count+1))
        msg_input.send_keys("pls beg")
        msg_input.send_keys(Keys.ENTER)
        beg_current = beg_cooldown+1
        beg_count+=1
    elif(dig_current <= 0):
        print("Digging for the {0} time".format(dig_count+1))
        msg_input.send_keys("pls dig")
        msg_input.send_keys(Keys.ENTER)
        dig_current = dig_cooldown+1
        dig_count+=1
    elif(hunt_current <= 0):
        print("Hunting for the {0} time".format(hunt_count+1))
        msg_input.send_keys("pls hunt")
        msg_input.send_keys(Keys.ENTER)
        hunt_current = hunt_cooldown+1
        hunt_count+=1
    elif(fish_current <= 0):
        print("Fishing for the {0} time".format(fish_count+1))
        msg_input.send_keys("pls fish")
        msg_input.send_keys(Keys.ENTER)
        fish_current = fish_cooldown+1
        fish_count+=1
    elif(dep_current <= 0):
        print("Depositing for the {0} time".format(dep_count+1))
        msg_input.send_keys("pls dep max")
        msg_input.send_keys(Keys.ENTER)
        dep_current = dep_cooldown+1
        dep_count+=1

    beg_current-=1
    dig_current-=1
    hunt_current-=1
    fish_current-=1
    dep_current-=1
print("Its Done!")