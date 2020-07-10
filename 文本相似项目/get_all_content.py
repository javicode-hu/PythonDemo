import codecs
import re
from bs4 import BeautifulSoup
import requests
from requests import RequestException

#获取可用的学生id和对应url
def get_dict():
    stu = []
    fp = codecs.open('data.txt', "r", encoding='utf8', errors='ignore')
    content = fp.read()
    p = re.compile(r'\d+\s+http://blog.sina.com.cn/u/\d+')
    for one in p.findall(content):
        one_data = one.split('\t')
        stu.append(one_data)
    fp.close()
    return stu

#获取网页源代码
def get_response(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

#获取对应id的博客内容并保存在文件
def get_txt(html,num):
   # soup = BeautifulSoup(html,'parser.html')
   all_pat = re.compile('<span class="SG_more"><a href="(.*?)" target="_blank">查看全文</a>&gt;&gt;</span>',re.S)
   try:
       txt_url = re.findall(all_pat,html)[0]
       html = get_response(txt_url)
       soup = BeautifulSoup(html,'html.parser')
       content = soup.find_all(attrs={'class':'articalContent'})[0].get_text()
       path = str(num)+'.txt'
       fp = open(path, 'w', encoding='utf8', errors='ignore')
       fp.write(content)
       fp.close()
   except IndexError:
       return None

if __name__ == '__main__':
    stu = get_dict()
    for item in stu:
        num = item[0]
        url = item[1]
        print(num,url)
        html = get_response(url)
        get_txt(html,num)
