#抓取美人志网站的图片
#罗旭阳，2019/02/05
import requests
from lxml import etree

page_url = "http://wenyixiaoqingxina.lofter.com/?page={}".format(page_num)

def  gethtml(url):
	#对页面进行解析
	html = etree.HTML(requests.get(url).content)
	#获取页面链接
	html_links = etree.xpath("//div[@class="img"]/a[@href]")
	return html_links
	pass

def write_content(content):
	file_name =


def main():
	html_links = gethtml(page_url)

	pass
