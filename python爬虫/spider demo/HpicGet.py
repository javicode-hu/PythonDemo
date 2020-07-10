import  requests
import re
import os
from requests import RequestException




def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<img id=".*?".*?src="(.*?)"',re.S)
    items = re.findall(pattern,html)
    return items

def save_to_img(url,root,path):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")

def get_page_url(url):
    html=get_one_page(url)
    pattern = re.compile('<li><a href="/dohtml/doticle/(.*?)" target="_blank"',re.S)
    urls = re.findall(pattern,html)
    return urls



def main(num):
    if(num==1):
        url_1 = 'http://www.dodorr.cc/dohtml/part/index17.html'
    else:
        url_1='http://www.dodorr.cc/dohtml/part/index17_'+str(num) +'.html'
    for url in get_page_url(url_1):
        url = 'http://www.dodorr.cc/dohtml/doticle/' +url
        html = get_one_page(url)
        parse_one_page(html)
        for item in parse_one_page(html):
            root = "F://Huangtu//"
            url =item
            path = root +  url.split('/')[-1]
            save_to_img(url, root, path)
main(10)