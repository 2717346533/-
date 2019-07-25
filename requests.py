import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
html = requests.get("http://jp.tingroom.com/yuedu/yd300p/",headers = headers)
html.encoding = 'utf-8'
print(html.text
