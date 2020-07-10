# coding:utf-8
import threading
import urllib.request
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests
from requests import RequestException
from bs4 import  BeautifulSoup
import  sys
import  os


def get_response(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url,headers=kv)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

# 通过返回的网页数据，过滤出文件名称和MP4路径
def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    cont = soup.select(".j-r-list-c")
    urlList =[]
    for item in cont:
        name = item.find('a').text
        pmUrl =item.select(' .j-video')[0].get('data-mp4')
        # 以元祖的形式添加到数组
        urlList.append((name,pmUrl))
    return urlList




# 拼接MP4保存的路径和文件名，这里用多线程的方法
def save_mp4():
    '''''
         判断当前脚本所在路径是否存在picture文件夹，这里用os模块，os.getcwd()获取当前文件的绝对路径
         使用os模块的该方法不用考虑所在系统是Mac还是windows
        '''
    filePath = os.path.join(os.getcwd(),'picture')
    if not os.path.exists(filePath):
        print("路径不存在")
        os.makedirs(filePath)
    url = 'http://www.budejie.com/video/'
    html = get_response(url)
    movieList =get_content(html)
    for item in movieList:
        if item[1]==None:
            continue
        for item in movieList:
            urllib.request.urlretrieve(item[1],'video\\%s.mp4' % (item[0]))
            movieList.pop(0)  # 删除已经有的
            # 判断要使用的名称是否过长，如果超过30的话，我们就截取，因为文件名过长保存的时候会报错
        #namestr = item[0].strip() if len(item[0])<30 else item[0].strip()[:27]+'...'
        # 拼接文件的绝对路径
        #mvPath = os.path.join(filePath, '%s.%s'%(item[0],item[1][-3:]))


# 保存MP4文件
def start_thr():
    # 通过多线程的方式下载MP4文件，增加下载速度
    thr = threading.Thread(target=save_mp4)
    # 启动线程
    thr.start()


def main():
   start_thr()
main()