import requests
import re
import os
from requests import RequestException


def parser_page(url): #获取网页源代码
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None


def get_url(html):
    pattern = re.compile('<div class="album-grid-item"><a href="(.*?)">',re.S)
    items = re.findall(pattern,html)
    print(items)
    return items


def get_one_detail(url):
    html = parser_page(url)
    pattern = re.compile('<a class="colorbox-gal" data-colorbox="true" href="(.*?)">',re.S)
    # pattern_name = re.compile('<div class="asset-caption"><p>(.*?)</p>',re.S)
    items = re.findall(pattern,html)
    # names = re.findall(pattern_name,html)
    return items




def save_img(url,root,path):
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
    pass


def main():

    url = "https://rhads.artstation.com/"
    itemurls=get_url(parser_page(url))
    for itemurl in itemurls:
        onepage_url = url + itemurl
        for item in get_one_detail(onepage_url):
            root = 'E://Artstation//rhads//'
            img_url = item
            path = root+item.split('/')[-1][-10:]+".jpg"
            print(path)
            save_img(img_url,root,path)





main()