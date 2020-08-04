from selenium import webdriver
import pandas as pd
# import json

driver = webdriver.Chrome()
# driver.get('https://protonmail.com/')
# driver.maximize_window()

text = pd.read_json('./ex.json')
# print(text)


driver.get(text.base_url[0])
driver.maximize_window()

for i in range(0,8):
	button = driver.find_element_by_xpath(text.steps[i].get('xpath'))
	driver.implicitly_wait(text.steps[i].get('wait'))
	if(text.steps[i].get('operation') == 'CLICK'):
		button.click()
	elif(text.steps[i].get('operation') == 'SEND_KEYS'):
		button.send_keys(text.steps[i].get('data').get('value'))


