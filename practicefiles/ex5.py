from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



def perform_op(element, operation, value):
	global para_count
	# print("passed value ", value, "para_count", para_count)
	if(i.get('operation') == 'CLICK'):
		element.click()
	elif(i.get('operation') == 'SEND_KEYS'):
		element.send_keys(data.get('value')[para_count])
		para_count = para_count + 1

try:
	directory = pd.read_json('/home/ankit/project/JSON_files/filedir.json')
	log = open('log.txt','w')
except Exception as e:
	log.write('Input : /home/ankit/project/JSON_files/filedir.json ,log.txt\n')
	log.write(str(e))


try:
	driver = webdriver.Chrome()
except Exception as e:
	log.write('Input : Driver Instance\n')
	log.write(str(e))

cnt = 0 
data_cnt = 0
para_count = 0

driver.maximize_window()

for itern,k in zip(directory.filedir,directory.datadir):
	try:
		file = pd.read_json(itern)
		data_file = pd.read_json(k)
	except Exception as e:
		log.write('Input : file, data_file\n')
		log.write(str(e))
	# print(file)
	print(cnt , file.base_url[0])

	try:
		if(cnt==0):
			driver.get(file.base_url[0])
		else:
			driver.execute_script("window.open()")
			driver.switch_to_window(driver.window_handles[cnt])
			driver.get(file.base_url[0])
	except Exception as e:
		log.write('Input : file.base_url\n')
		log.write(str(e))

	data_cnt = 0
	for data in data_file.obj1:
		para_count=0
		for i in file.steps:
			try:
				element = driver.find_element_by_xpath(i.get('xpath'))
				driver.implicitly_wait(i.get('wait'))
			except Exception as e:
				log.write('Input : xpath\n')
				log.write(str(e))
			# print(para_count)
			try:
				perform_op(element,i.get('operation'),data.get('value'))
			except Exception as e:
				log.write('Input : value\n')
				log.write(str(e))

			# para_count = para_count + 1
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
		log.write("Input : Driver Instance\n")
		log.write(str(e))

driver.close()
