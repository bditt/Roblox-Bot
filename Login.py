import random
import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
random.seed(time.localtime)

#Setup Selenium
path = 'C:\\Users\\patron\\Desktop\\Chrome Driver\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(path)
driver.get("https://roblox.com/login")
assert "Roblox" in driver.title

#Write to the username field.
username_field = driver.find_element_by_id("login-username")
username_field.clear()
username_field.send_keys("AspectNetwork01")

#Write to the password field.
password_field = driver.find_element_by_id("login-password")
password_field.clear()
password_field.send_keys("AspectNetwork01AspectNetwork01")

#Click the signup button.
login_button = driver.find_element_by_id("login-button")
login_button.click()

try:
    WebDriverWait(driver, 30).until(lambda x: 'Home' in driver.title)
except TimeoutException as e:
    print(e)
    pass

rbxcookie = driver.get_cookie(".ROBLOSECURITY")
print(rbxcookie["value"])
currentcookielog = open("currentcookie.log", "a")
currentcookielog.write(rbxcookie["value"])