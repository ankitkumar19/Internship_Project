from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import requests

driver = webdriver.Chrome()
driver.get('https://www.spotify.com/')
driver.maximize_window()

login = driver.find_element_by_xpath('/html/body/div[2]/div/header/div/nav/ul/li[6]/a')
driver.implicitly_wait(10)
login.click()

username = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/div/input')
driver.implicitly_wait(10)
username.send_keys('ankit.bhushan19@gmail.com')

password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/div/input')
driver.implicitly_wait(10)
password.send_keys('Ankit@123456')

login_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button')
driver.implicitly_wait(10)
login_button.click()

dismiss_popup = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div[2]/button[2]')
driver.implicitly_wait(10)
dismiss_popup.click()

# # body = driver.find_element_by_tag_name("body")
# # body.send_keys(Keys.CONTROL + 't')
# new_url = 'https://www.spotify.com/in/'
# driver.implicitly_wait(10)
# driver.execute_script('''window.open("https://www.spotify.com/in/","_blank");''')

