#获取浏览器上面的图片
#罗旭阳，2019/02/04
import requests
from bs4 import BeautifulSoup
import time
#from PIL import Image

#获取页面代码
def getHtml(url):
	html = requests.get(url)
	html.encoding = "utf-8"
	print(html.raise_for_status)
	bsObj = BeautifulSoup(html.text, "lxml")
	return bsObj

def getLinks(html):
	image_content_tags = html.find_all("a", class_="img-content")
	links = []
	for image_content in image_content_tags:
		links.append(image_content["href"])

	return links



def main():
	question = "美女"
	num = 1
	for page_num in range(10):
		time.sleep(3)
		url = "https://mijisou.com/?category_images=1&q=" + str(question) + "&pageno=" + str(page_num) + "&time_range=&language=zh-CN"
		html = getHtml(url)
		links = getLinks(html)
	#print(links)

		for link in links[1:]:
			html = requests.get(link)
			with open("d:/picture/" + str(num) + ".jpg", "wb") as fObj:
				fObj.write(html.content)
				fObj.close()
				print("piture " + str(num) + " save successfully")
				num += 1
		#else:
		#	num += 1
		#	print(html.raise_for_status)
		#	print("now is " + str(num) + "picture.")
	pass

main()
input()
