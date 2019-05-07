# 爬取豆瓣电影数据
# 了解ajax的爬取方式
# https://movie.douban.com/

from urllib import request
import json
import requests

base_url = 'https://www.toutiao.com/search/?'
# url信息：interval_id表示排名段（可自行修改），limit限制20个
#def get_index(offset):
    #参数字典
params = {
    'aid':'24',
    'offset':20,
    'keyword':'街拍',
    'autoload':'tre',
    'count':'20',
    'cur_tab':'1',
    'from':'search_tab',
    'pd':'synthesis',
    }
    #html = requests.get(base_url, params = params)
    #pass

rsp = requests.get(base_url, params=params)
print(type(rsp.content))
#date = str(rsp.content)
#date = date[2:-3]
#print(date.decode())
#print(type(str(rsp.content)))
#print(rsp.content.decode())
data = rsp.content.decode("utf-8", "ignore").replace("\xa9", "")
data = str(data)[2:-3]
print(data)
#data = json.loads(data)