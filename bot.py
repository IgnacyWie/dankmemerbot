from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
from random import random, randint
import os

# User Variables
UserEmail = os.environ.get('EMAIL') #insert your password in this variable
UserPassword = os.environ.get('DISCORDPASSWORD') #insert your password in this variable
Serverlink = ""
Textxpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div/div[3]/div[2]"
fricklist = ["f", "r", "i", "c", "k"]

# Opening discord link
driver = webdriver.Chrome() #insert your path into those brackets
driver.get(Serverlink)

# Logging in
email = driver.find_element_by_name("email")
email.send_keys(UserEmail)
password = driver.find_element_by_name("password")
password.send_keys(UserPassword)
login = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]")
login.click()
time.sleep(5)

chat = driver.find_element_by_xpath(Textxpath)

# Sending pls beg every 45 seconds
def beg():    
    while True:
        chat.send_keys("pls beg")
        chat.send_keys(Keys.ENTER)
        time.sleep(45)

def frick():
    time.sleep(1)
    while True:
        rand = randint(0, len(fricklist)-1)
        chat.send_keys("pls pm")
        chat.send_keys(Keys.ENTER)
        time.sleep(1)
        chat.send_keys(fricklist[rand])
        chat.send_keys(Keys.ENTER)
        time.sleep(63)
def fishunt():
    time.sleep(3)
    while True:
        chat.send_keys("pls hunt")
        chat.send_keys(Keys.ENTER)
        chat.send_keys("pls fish")
        chat.send_keys(Keys.ENTER)
        time.sleep(64)

def deposit():
    time.sleep(4)
    while True:
        chat.send_keys("pls dep all")
        chat.send_keys(Keys.ENTER)
        time.sleep(3600)

thread1 = threading.Thread(target = beg)
thread1.start()
time.sleep(3)
thread2 = threading.Thread(target = frick)
thread2.start()
thread3 = threading.Thread(target = deposit)
thread3.start()
thread4 = threading.Thread(target = fishunt)
thread4.start()
