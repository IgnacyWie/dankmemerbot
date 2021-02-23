from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
from random import randint
PATH = "C:\Program Files (x86)\chromedriver.exe"
# User Variables
UserEmail = ""
UserPassword = ""
Serverlink = ""
Textxpath = "/html/body/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div/div[3]/div[2]/div"

# Opening discord link
driver = webdriver.Chrome(PATH)
driver.get(Serverlink)

# Logging in
email = driver.find_element_by_name("email")
email.send_keys(UserEmail)
password = driver.find_element_by_name("password")
password.send_keys(UserPassword)    
login = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]")
login.click()
time.sleep(5)

#list of meme types (postmeme)
fricklist = ["f", "r", "i", "c", "k"]

chat = driver.find_element_by_xpath(Textxpath)

# Sending pls beg every 45 seconds

def beg():
    while True:
        chat.send_keys("pls beg")
        chat.send_keys(Keys.ENTER)
        time.sleep(48)
# Sending pls fish every 60 seconds
# Sending pls hunt every 60 seconds

def fishunt():
    while True:
        chat.send_keys("pls fish")
        chat.send_keys(Keys.ENTER)
        chat.send_keys("pls hunt")
        chat.send_keys(Keys.ENTER)
        time.sleep(63)
# Sending pls daily every 24 hour
        
def daily():
    while True:
        chat.send_keys("pls daily")
        chat.send_keys(Keys.ENTER)
        time.sleep(86405)
# Sending pls postmeme every 60 seconds and randomly choosing a meme
    
def frick():
    while True:
        rand = randint(0, len(fricklist)-1)
        chat.send_keys("pls pm")
        chat.send_keys(Keys.ENTER)
        time.sleep(1)
        chat.send_keys(fricklist[rand])
        chat.send_keys(Keys.ENTER)
        time.sleep(63)
# Depositing all money to the bank every hour
        
def deposit():
    while True:
        chat.send_keys("pls dep all")
        chat.send_keys(Keys.ENTER)
        time.sleep(600)
# Taking care of your pet

def pet():
    while True:
        for i in range(3):
            chat.send_keys("pls pet feed")
            chat.send_keys(Keys.ENTER)
        for i in range(2):
            chat.send_keys("pls pet wash")
            chat.send_keys(Keys.ENTER)
        time.sleep(86410)
# Failing your work every 30 minutes

def job():
    while True:
        chat.send_keys("pls work")
        chat.send_keys(Keys.ENTER)
        time.sleep(2)
        for i in range(3):
            chat.send_keys("IgnacyNoob")
            chat.send_keys(Keys.ENTER)
        time.sleep(1800)
# Sending pls search every 30 seconds

# Threading beg fishunt frick deposit job

thread1 = threading.Thread(target = beg)
thread1.start()
time.sleep(3)
thread2 = threading.Thread(target = frick)
thread2.start()
thread3 = threading.Thread(target = deposit)
thread3.start()
thread4 = threading.Thread(target = fishunt)
thread4.start()
