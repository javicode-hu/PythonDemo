#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/27 23:25
# @Author : hujiawei
# @File : demo.py
# @Software: PyCharm
import random
import time
from multiprocessing.pool import Pool
import ipsGet
import pymongo
import requests

ip_pool = ['114.101.19.158:65309', '121.69.37.6:9797', '119.33.64.147:80', '122.4.29.178:9999', '171.12.112.210:9999', '1.197.203.70:9999', '123.163.96.87:9999', '117.91.252.182:9999', '1.198.72.59:9999', '117.91.251.11:9999', '121.233.207.151:9999', '182.35.87.155:9999', '111.231.140.109:8888']
user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

#获取网页源代码
def get_response_bypost(url):

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                     ' (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'origin':'https://music.163.com',
        'accept': '*/*',
        'accept - encoding': 'gzip, deflate, br',
    }
    data = {
        'params':'6mtGyXOZ2Eq7XlKAocIDuBXJ7FXBzFmJ/3TR79m9He8A33WFa72/+FNu5g48QXsE'
                 '4ojBwvLkPaqQt+tsBqFFxoPUjN1Mw4wdx3xBwnW4+6b+jTDOnoPu/w0OPNpQD0lXT'
                 '8fyHndWim6nk76P0YzTzrfApeZzW2fG8qUjItjyFV9Id4/SjGnVA/ljHWoWke/A',
        'encSecKey':'9bf01e6270965d603ef483195dbfdbee33bd00a26bf8dcc5589b296eeca39'
                    'c74e5d3a773940e6f57e9e0d75c871e4e53e778ceb9679a4985681e41dea6c'
                    '6bd3ebc01c6a9e9fb3360740844488d0ee73adf77f49cdb9369e3007828aae4'
                    '4c54c6951d905ebc71f0a09a43a1901f256ddac33e58c361178e9f1338a71db70c7877',
    }
    try:
        response  =requests.post(url,headers=headers,data=data)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
        get_response_byget(url)

#获取网页源代码
def get_response_byget(url):
    try:
        headers = {
            'accept': '*/*',
            'accept - encoding': 'gzip, deflate, br',
            'Connection': "keep-alive",
            'Host': "music.163.com",
            'user-agent': random.choice(user_agents),
        }
        proxies = {
            "http": random.choice(ip_pool),
        }
        response = requests.get(url,headers=headers,proxies=proxies)
        if response.status_code==200:
            print(response.json())
            return response.json()
    except Exception as e:
        print("error",e.args)

#解析评论信息
def get_comments_info(url):
    json = get_response_byget(url)
    data_lists =[]
    comments = json['comments']
    for user in comments:
        time = timeStamp(int(user['time']))
        nickname  = user['user']['nickname']
        likecount = user['likedCount']
        content = user['content']
        info = {
            "nickname":nickname,
            'content':content,
            'likecount':likecount,
            'time':time,
        }
        data_lists.append(info)
    write_into_mongo(data_lists)


#13位时间戳转成正常格式的时间
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def write_into_mongo(datas):
    """
    :param data: 遍历字典数据
    :return:
    """
    client = pymongo.MongoClient('localhost',27017)
    db = client['wyy']
    collection = db['Five_Hundred_Miles']
    try:
        if collection.insert_many(datas):
            print('成功插入', len(datas), '条数据')
    except Exception as e:
        print("插入数据异常",e)


def multi_process_do(url_list):
    """
    多进程调用函数
    :return:
    """
    begin = time.time()
    pool = Pool(processes=3)
    pool.map(get_comments_info,url_list)
    end = time.time()
    print("耗时：%s" % (end-begin))




if __name__ == '__main__':
    url_list = []
    for i in range(1,10000,19):
        url = "http://music.163.com/api/v1/resource/comments/R_SO_4_27759600?limit=19&offset={}".format(i)
        url_list.append(url)
    multi_process_do(url_list)