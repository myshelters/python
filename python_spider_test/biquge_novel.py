#笔趣阁小说抓取
#罗旭阳，2019/01/31
import requests
#from bs4 import BeautifulSoup
from lxml import etree
url = "https://www.biquge5200.cc/76_76490/"
#获取小说链接
def get_links(url):
	'''input url return links'''
	html = requests.get(url)
    html = str(html.text)
	lxmlObj = etree.HTML(html)
	links = lxmlObj.xpath('/html/body/div[1]/div[6]/div/dl/dd')
	#print(html.text)
	links = bsObj.find_all('dd')
	#查看最后一部分是什么

	for link in links :
		yield link

links = get_links(url)
for link in links:
	print(link)
