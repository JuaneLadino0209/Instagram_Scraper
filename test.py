from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.set_window_size(900,900)
#browser.maximize_window()
#sleep(3)
browser.get("https://www.instagram.com/")