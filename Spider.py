import re
import requests

#读取源代码文件
f = open('source.txt',encoding='gb18030',errors='ignore')
html = f.read()
f.close()

#匹配图片网址
pic_url = re.findall('img class="uptodate-img" src="(.*?)" ',html,re.S)
i = 0
for each in pic_url:
    print("now downloading:" + each)
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.png','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
