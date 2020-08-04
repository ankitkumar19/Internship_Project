from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


directory = pd.read_json('/home/ankit/project/JSON_files/filedir.json')
# for i in directory.datadir:
# 	# print(i)
# 	file = pd.read_json(i)
# 	# print(file.map)
# 	for j in file.obj1:
# 		if(file.map[0] == 2):
# 			print(j.get("value")[0])


driver = webdriver.Chrome()



driver.maximize_window()
cnt = 0 
data_cnt = 0
para_count = 0
for itern,k in zip(directory.filedir,directory.datadir):
	file = pd.read_json(itern)
	data_file = pd.read_json(k)
	# print(file)
	print(cnt , file.base_url[0])
	if(cnt==0):
		driver.get(file.base_url[0])
	else:
		driver.execute_script("window.open()")
		driver.switch_to_window(driver.window_handles[cnt])
		driver.get(file.base_url[0])
	data_cnt = 0
	for data in data_file.obj1:
		para_count=0
		for i in file.steps:
			button = driver.find_element_by_xpath(i.get('xpath'))
			driver.implicitly_wait(i.get('wait'))
			if(i.get('operation') == 'CLICK'):
				button.click()
			# elif(i.get('operation') == 'SEND_KEYS' and data_file.map[0] == 1): 
			# 	button.send_keys(data.get('value'))
			elif(i.get('operation') == 'SEND_KEYS'):
				button.send_keys(data.get('value')[para_count])
				para_count = para_count + 1
		if(data_cnt < len(data_file.obj1)-1):
			data_cnt = data_cnt+1
			print(cnt , file.base_url[0] , data.get('value'))
			driver.execute_script("window.open()")
			driver.switch_to_window(driver.window_handles[cnt+data_cnt])
			driver.get(file.base_url[0])
	cnt = cnt+data_cnt+1
	try:
		driver.implicitly_wait(10)
		driver.switch_to_alert.dismiss()
	except Exception as e:
		print(e)

# driver.close()