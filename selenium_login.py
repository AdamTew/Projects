from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

browser = webdriver.Firefox()

browser.get('webpage.com')

username = browser.find_element_by_name("username")
username.send_keys("username")

password = browser.find_element_by_name("password")
password.send_keys("password")

browser.find_element_by_id("submit_login").click()

browser.get('http://app.webinarjam.com/members/evergreen/webinar/analytics')

html = browser.page_source
ids = re.findall("(?<=\")[0-9a-z]+(?=\")", html)
