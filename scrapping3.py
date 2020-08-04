import bs4
import requests

res = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic+cards')

soup = bs4.BeautifulSoup(res.text,'lxml')

containers = soup.find_all('div',{'class' : 'item-cell'})

f = open('scrap_data1.csv',"w")

headers = 'Brand, Product, Shipping\n'
f.write(headers)

for container in containers:
	brand = container.div.div.a.img['title']
	title = container.find_all('a',{'class':'item-title'})[0].text
	shipping = container.find_all('li',{'class':'price-ship'})[0].text
	print(brand)
	print(title)
	print(shipping)
	print( )

	f.write(brand+ ","+ title.replace(",","|")+ "," +shipping + "\n")
f.close()

# print(containers[0].find_all('li',{'class':'price-ship'})[0].text)
