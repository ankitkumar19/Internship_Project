import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')	

title = soup.select('.mw-headline')
for t in title:
	print(t.text)