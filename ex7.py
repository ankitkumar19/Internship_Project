from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
import bs4
import requests
from PIL import Image



def perform_op(element, operation, value):
	global para_count
	# print("passed value ", value, "para_count", para_count)
	if(i.get('operation') == 'CLICK'):
		element.click()
	elif(i.get('operation') == 'SEND_KEYS'):
		element.send_keys(data.get('value')[para_count])
		para_count = para_count + 1
	elif(i.get('operation') == 'COMBOBOX'):
		select = Select(element)
		select.select_by_value(data.get('value')[para_count])
		para_count = para_count + 1
	elif(i.get('operation') == 'DROPDOWN'):
		select = Select(element)
		select.select_by_visible_text(data.get('value')[para_count])
		para_count = para_count + 1




def init_output(driver):
	url = driver.current_url
	res = requests.get(url)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	get_output(soup,data.get('attribute'),data.get('class'),scrap)



def get_output(soup,attribute,class_name,scrap):
	global para_count_output
	print(attribute , class_name , para_count)
	headings = soup.find_all(attribute[para_count_output],{'class':class_name[para_count_output]})
	para_count_output = para_count_output + 1
	for heading in headings:
		print(heading.text)
		scrap.write(str(heading.text))





def find_element(method,i):
	if(method == 'xpath'):
		# print(type(driver.find_element_by_xpath(i.get('xpath'))))
		return driver.find_element_by_xpath(i.get('xpath'))
	elif(method == 'id'):
		# driver.implicitly_wait(10)
		print(type(driver.find_element_by_id(i.get('id'))))
		return driver.find_element_by_id(i.get('id'))
	elif(method == 'name'):
		return driver.find_element_by_name(i.get('name'))
	elif(method == 'link_text'):
		return driver.find_element_by_link_text(i.get('link_text'))
	elif(method == 'partial_link_text'):
		return driver.find_element_by_partial_link_text(i.get('partial_link_text'))
	elif(method == 'tag_name'):
		return driver.find_element_by_tag_name(i.get('tag_name'))
	elif(method == 'class_name'):
		return driver.find_element_by_class_name(i.get('class_name'))
	elif(method == 'css_selector'):
		return driver.find_element_by_css_selector(i.get('css_selector'))



def get_captcha(driver,path):
	driver.switch_to.frame("Main")
	element = find_element(data_file.get('method')[0],i)
	location = element.location
	size = element.size
	driver.save_screenshot(path)

	image = Image.open(path)
	left = location['x']
	top = location['y']+140
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']+140
	image = image.crop((left,top,right,bottom))

	image.save(path,'png')


try:
	directory = pd.read_json('/home/ankit/project/JSON_files/filedir.json')
	log = open('log.txt','w')
	scrap = open('scrap.txt','w')
except Exception as e:
	log.write('Input : /home/ankit/project/JSON_files/filedir.json, log.txt\n')
	log.write(str(e))


try:
	driver = webdriver.Chrome()
except Exception as e:
	log.write('Input : Driver Instance\n')
	log.write(str(e))



cnt = 0 
data_cnt = 0
para_count = 0
para_count_output = 0

driver.maximize_window()




for itern,k in zip(directory.filedir,directory.datadir):
	try:
		file = pd.read_json(itern)
		data_file = pd.read_json(k)
	except Exception as e:
		log.write('Input : file, data_file\n')
		log.write(str(e))
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
				if(i.get('operation') != "SCRAPING" and i.get('operation') != 'CAPTCHA'):
					element = find_element(data_file.get('method')[0],i)
					driver.implicitly_wait(i.get('wait'))

					try:
						perform_op(element,i.get('operation'),data.get('value'))
					except Exception as e:
						log.write('Input : value\n')
						log.write(str(e))

				elif(i.get('operation') == 'CAPTCHA'):
					# element = find_element(data_file.get('method')[0],i)
					driver.implicitly_wait(i.get('wait'))
					get_captcha(driver,'./captcha.png')

				else:
					init_output(driver)

			except Exception as e:
				log.write('Input : xpath\n')
				log.write(str(e))


			# para_count = para_count + 1
		if(data_cnt < len(data_file.obj1)-1):
			data_cnt = data_cnt+1
			# print(cnt , file.base_url[0] , data.get('value'))
			driver.execute_script("window.open()")
			driver.switch_to_window(driver.window_handles[cnt+data_cnt])
			driver.get(file.base_url[0])
	cnt = cnt+data_cnt+1

time.sleep(10)
driver.quit()

