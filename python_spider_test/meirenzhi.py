#爬取美人志图片
#author：@shelter
#2019/3/29
import requests
import re
import json

def get_html(url):
	
	respond = requests.get(url + str(PageNum))
	if respond.status_code == 200:
		return respond.text
	else:
		return respond.raise_for_status
	pass

def parser_html(html):
	content = re.compile('<div class="m-post m-post-img .*?>.*?<a class="img" href="(.*?)">.*?</div', re.S)
	items = re.findall(content, html)
	for item in items:
		#print(item)
		yield{
		"img_index_url": item[:]
		}

def write_url(item):
	with open("UrlList.txt", "a", encoding="utf-8") as f:
		f.write(json.dumps(item, ensure_ascii=False))

def main():
	url = "http://loftermeirenzhi.lofter.com/?page="
	html = get_html(url)
	#print(html)
	file_num = 1
	for item in parser_html(html):
		print(file_num)
		print(item)
		write_url(item)
		file_num = file_num +1


main()