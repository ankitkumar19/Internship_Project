from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://slcm.manipal.edu/loginForm.aspx')
driver.maximize_window()

username = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[1]/input')
driver.implicitly_wait(10)
username.send_keys('170905634')

password = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[2]/input')
driver.implicitly_wait(10)
password.send_keys('Ankit@123456')

signin = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div/div[3]/input')
signin.click()