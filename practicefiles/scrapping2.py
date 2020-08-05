import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')

for i in soup.find_all('a',href = True):
	if(i['href'][:2]=='//'):
		print("www.google.com"+i['href'][2:])
	if(i['href'][0]!='#'):
		print(i['href'])
