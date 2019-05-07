#抓取bilibili排行榜内容
#罗旭阳，2019/01/30
import requests
import re
from bs4 import BeautifulSoup
import json

def getPage(url):
	html = requests.get(url)
	print(html.encoding)
	bsObj = BeautifulSoup(html.text, "lxml")
	return bsObj


def HtmlContent(html):
	items = html.find_all("li", class_="rank-item")
	for item in items:
		yield{
		"index": item.find('div', class_="num").string,
		"title": item.find('a', class_="title").string
		}

	return items

def write_content(content):
	with open("D:/bilibili_list.txt", "a", encoding="utf-8") as fObj:
		fObj.write(json.dumps(content, ensure_ascii=False))
		fObj.close()
		print("write successful")
	pass
def main():
	url = "https://www.bilibili.com/ranking/bangumi/13/1/3/?spm_id_from=333.334.b_72616e6b696e675f74696d696e675f62616e67756d69.11"
	html_source = getPage(url)
	for item in HtmlContent(html_source):
		print(item)
		write_content(item)
	pass

main()
input()
