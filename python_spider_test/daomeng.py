import requests

url = "http://pingma.qq.com/mstat/report/?index=1552644538"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; M040 Build/JRO03H)',
    'Host': '120.55.151.61',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '207',
    }

html = requests.post(url, headers = headers, verify = False )
print(html.raise_for_status)
print(html.text)
#data = html.json()
#print(html.headers)
#print(html.raise_for_status)
#print(data)