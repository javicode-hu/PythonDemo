import threading
import time
import  requests
import re
import os
import random
from requests import RequestException



def parser_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

def get_page_url(html):
    pattern = re.compile('<a href="(.*?)" target="_blank">', re.S)
    items = re.findall(pattern, html)
    return items

def get_one_page(url):
    html = parser_one_page(url)
    pattern = re.compile('<img src="(.*?)" />', re.S)
    gif_urls = re.findall(pattern,html)
    return gif_urls

def save_to_file(url,root,path):
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

def download(n):
    numbers = range(n)
    def thread_download(n):
        url = 'https://www.657aa.com/htm/giflist0/3.htm'
        html = parser_one_page(url)
        # for item in get_page_url(html):
        item = get_page_url(html)[n]
        page_url = 'https://www.657aa.com'+item
        files = get_one_page(page_url)
        # stop = len(files) //len(numbers)
        # directory = files[n * stop: (n + 1) * stop]
        for gif_url in files:
            root = "F://Hgif//"
            path = root+str(random.randint(0,1000000))+'.gif'
            save_to_file(gif_url,root,path)

    thread_list=[]
    for i in range(5):
        t = threading.Thread(target=thread_download, args=(i,))
        t.setDaemon(True)
        thread_list.append(t)

    for t in thread_list:
        t.start()
        time.sleep(random.randint(0,3))

    for t in thread_list:
        t.join()  # join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。

download(8)