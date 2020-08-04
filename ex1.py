from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# import json

driver = webdriver.Chrome()
# driver.get('https://protonmail.com/')
# driver.maximize_window()

text = pd.read_json('./ex1.json')
# print(text.obj1.get("steps"))

# for itern in text.obj1:
# 	print(itern.get('base_url'))
# 	print("\n")
	

# driver.get(text.obj1.get("base_url"))
driver.maximize_window()
cnt = 0 
for itern in text.obj1:
	print(cnt , itern.get('base_url'))
	if(cnt==0):
		driver.get(itern.get('base_url'))
	else:
		driver.get(itern.get('base_url'))
		# ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
		# url = itern.get('base_url')
		# print(url)
		# driver.execute_script('''window.open("url","_blank");''')

	for i in itern.get("steps"):
		button = driver.find_element_by_xpath(i.get('xpath'))
		driver.implicitly_wait(i.get('wait'))
		if(i.get('operation') == 'CLICK'):
			button.click()
		elif(i.get('operation') == 'SEND_KEYS'):
			button.send_keys(i.get('data').get('value'))
	cnt = cnt+1
	# driver.execute_script('''window.open("https://www.spotify.com/in/","_blank");''')


