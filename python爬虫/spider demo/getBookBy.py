import os
import sys

import requests
from requests import RequestException
import  re


#获取网页源代码
def get_response(isbn):
    url = "http://api.douban.com/book/subject/isbn/{}".format(isbn)
    try:
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

def get_book_url(html):
    root = "C://Users//16474//Desktop//数据库//"
    name_pat = re.compile('<db:attribute name="title">(.*?)</db:attribute>',re.S)
    name = re.findall(name_pat,html)[0]
    author_pat = re.compile('<db:attribute name="author">(.*?)</db:attribute>',re.S)
    author = re.findall(author_pat,html)[0]
    press_pat = re.compile('<db:attribute name="publisher">(.*?)</db:attribute>',re.S)
    press = re.findall(press_pat,html)[0]
    date_pat  =re.compile('<db:attribute name="pubdate">(.*?)</db:attribute>',re.S)
    date = re.findall(date_pat,html)[0]
    isbn_pat = re.compile('<db:attribute name="isbn13">(.*?)</db:attribute>',re.S)
    isbn = re.findall(isbn_pat,html)[0]
    price_pat = re.compile('<db:attribute name="price">(.*?)元</db:attribute>',re.S)
    price = re.findall(price_pat,html)[0]
    brief_pat =re.compile('<summary>(.*?)</summary>',re.S)
    brief = re.findall(brief_pat,html)[0].replace('\n','')
    photo_pat = re.compile('rel="alternate"/>\s+<link href="(.*?)" rel="image"/>',re.S)
    photo = re.findall(photo_pat,html)[0]
    photo_name = photo.split('/')[-1]
    path = root +photo_name
    save_to_img(photo,root,path)
    print(name)
    print(author)
    print(press)
    print(date)
    print(isbn)
    print(price)
    print(brief)
    print(path)

def save_to_img(url,root,path):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                # print("图片保存成功")
        else:
            # print("文件已存在")
             return
    except:
        # print("爬取失败")
        return



if __name__ == '__main__':
    isbn  =sys.argv[1]
    html = get_response(isbn)
    get_book_url(html)

