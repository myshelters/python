#获取ajax页面
#shelter，2019/02/10
import requests
import json
base_url = 'https://www.toutiao.com/search/?'

#输出20个项目的页面
def get_pages(offset):
	'''input offset refresh pages, return page'''
	#参数字典
	params = {
	'aid':'24',
	'offset':offset,
	'keyword':'街拍',
	'autoload':'tre',
	'count':'20',
	'cur_tab':'1',
	'from':'search_tab',
	'pd':'synthesis',
	}
	#输出参数
	response = requests.get(base_url, params=params)
	print(type(response.text))
	#解析编码为utf-8格式
	print(str(response.content.decode().replace("\xa9", "")))
	html_str = response_content[2:-3]
	return html_str
	pass




get_pages(20)
input()
