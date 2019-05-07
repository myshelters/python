# -*- coding:utf-8 -*-
#获取bilibili用户名称
import requests
from bs4 import BeautifulSoup
def  get_content(url):
	response = requests.get(url).text
	soup = BeautifulSoup(response, "lxml")
	print(soup.prettify.decode())
	#content = soup.find_all("div", class = "h-info")
	#return content
	pass

def main():
	url = "https://space.bilibili.com/32172331"
	content = get_content(url)
	print(url)

main()