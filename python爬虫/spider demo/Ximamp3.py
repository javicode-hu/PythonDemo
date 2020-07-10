# 抓取喜马拉雅的音频信息 存储MongoDB数据库
import threading

import requests
from bs4 import BeautifulSoup
import re
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
def get_detail_ur():
    start_urls =['http://www.ximalaya.com/dq/{}'.format(pn) for pn in range(1,85)] # 列表推导式
    for start_url in start_urls:
        response = requests.get(start_url,headers = headers).text
        soup = BeautifulSoup(response,'lxml')
        for item in soup.find_all('div',class_='discoverAlbum_item'):
            content = {
                'href':item.a['href'],
                'title':item.img['alt'],
                'img_url':item.img['src']
            }
            print('正在下载{}频道'.format(item.img['alt']))
            get_mp3(item.a['href'],item.img['alt'])
            time.sleep(1)
        break

def get_mp3(url,title):
    response = requests.get(url,headers =headers).text
    pattern = re.compile('<div class="personal_body" sound_ids="(.*?)">',re.S)
    num_lists = re.findall(pattern,response)[0].split(',')
    print(title+'频道存在{}个音频'.format(len(num_lists)))
    mkdir(title)
    os.chdir('F:\\xmly\\'+title)  # 切换到指定目录
    for id in num_lists:
        json_url = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
        html = requests.get(json_url,headers = headers).json()
        mp3_url = html.get('play_path')
        mp3_title =html.get('title')
        downlaod(mp3_url,mp3_title)
        print('{}下载成功'.format(mp3_title))


def mkdir(title):
    '''
    对给定的titl创建对应的文件夹
    :return: 
    '''
    path = title.strip() #去空格
    filePath = os.path.join('F:\\xmly\\',path)
    if not os.path.exists(filePath):
        print("路径不存在，创建{}文件夹".format(title))
        os.makedirs(filePath)
        return True
    else:
        print('文件夹已存在')
        return False

def downlaod(url,title):
    content = requests.get(url,headers= headers).content  #二进制数据
    name = title+'.m4a'
    with open(name,'wb') as file:
        file.write(content)

# 保存MP3文件
def start_thr():
    # 通过多线程的方式下载MP4文件，增加下载速度
    thr = threading.Thread(target=get_detail_ur())
    # 启动线程
    thr.start()


if __name__ == '__main__':   # 判断是不是当前文件执行
    start_thr()
