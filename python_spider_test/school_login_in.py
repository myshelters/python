#登陆校园网选课
#罗旭阳，2019/02/09
import requests
from lxml import etree
cookies = "UM_distinctid=1676f2d75cc9-07b…onId=yo5olk30f5vxdx55b2153ffz"
url = "http://kmustjwcxk1.kmust.edu.cn/jwweb/MAINFRM.aspx"


def postHtml(url , cookies = cookies):
	html = requests.post(url, cookies = cookies, )
	#lxml 解析后的网页
	return html.content
	pass

def main():
	html = postHtml(url,)
	print(html.status_code)

main()