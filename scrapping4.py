import bs4
import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
driver.maximize_window()

search = driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/div/input')
driver.implicitly_wait(10)
search.send_keys('India')

search_button = driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button')
# driver.implicitly_wait(10)
search_button.click()

url = driver.current_url
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text,'lxml')

# headings = soup.find_all('h2.span')
headings = soup.find_all('li',{'class':'toclevel-1'})

for heading in headings:
	print(heading.text)