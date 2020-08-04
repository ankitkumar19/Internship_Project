from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://protonmail.com/')
driver.maximize_window()

login = driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div/div[2]/ul/li[8]/a')
driver.implicitly_wait(10)
login.click()

username = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/form/div[1]/input')
driver.implicitly_wait(10)
username.send_keys('ankitkumar1999')

password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/form/div[1]/div[1]/input')
driver.implicitly_wait(10)
password.send_keys('manganpur')

button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/form/div[1]/div[2]/div/button')
driver.implicitly_wait(20)
button.click()

compose = driver.find_element_by_xpath('/html/body/div[2]/div[1]/section/button')
driver.implicitly_wait(10)
compose.click()

to = driver.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[2]/form/div/div/div/input')
driver.implicitly_wait(20)
to.send_keys('ankit.bhushan19@gmail.com')

subject = driver.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[5]/input')
driver.implicitly_wait(10)
subject.send_keys('Automated hi')

# matter = driver.find_element_by_xpath('/html/body/div[1]')
# driver.implicitly_wait(10)
# matter.send_keys('hi')

send = driver.find_element_by_xpath('/html/body/div[2]/form[1]/div/footer/div/button[3]')
driver.implicitly_wait(10)
send.click()