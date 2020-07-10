import json
import random
import re
import threading
import time

from bs4 import BeautifulSoup
import requests
from requests import RequestException


def randHeader():
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header

def randIp():
    pro =['139.199.38.182:8118', '222.52.142.244:8080', '219.246.90.204:3128', '222.221.11.119:3128', '61.176.223.7:58822', '123.157.206.135:80', '101.236.44.52:8866', '163.125.64.218:9797', '61.135.217.7:80', '121.69.37.6:9797', '101.236.57.99:8866', '58.53.128.83:3128', '115.28.209.249:3128', '118.31.79.226:3128', '125.46.0.62:53281', '111.230.183.90:8000', '180.104.147.231:8123', '119.51.89.18:1080', '219.238.186.188:8118', '60.216.101.46:59351', '61.135.155.82:443', '183.172.131.4:8118', '218.14.115.211:3128', '183.3.150.210:41258', '221.205.88.61:9797', '118.187.58.34:53281', '119.123.246.123:9000', '58.63.112.186:32231', '61.234.37.106:8080', '122.115.78.240:38157', '222.74.61.98:53281', '61.183.233.6:54896', '110.179.68.31:8123', '59.32.37.175:8010', '124.235.181.175:80', '117.114.149.10:43727', '116.22.59.48:808', '113.200.214.164:9999', '115.223.95.22:8010', '106.12.150.213:808', '112.98.126.100:41578', '183.129.207.82:18118', '112.95.205.124:8888', '183.6.120.29:1080', '182.88.151.246:9797', '122.227.139.170:3128', '119.123.172.157:9797', '114.112.84.197:39560', '101.76.252.73:1080', '115.219.109.210:8010', '117.21.191.151:61007', '59.37.33.62:54474', '113.110.200.88:9797', '218.17.253.106:60004', '180.140.191.233:36820', '119.254.94.123:50972', '202.103.12.30:60850', '182.88.213.201:8123', '122.237.106.134:80', '114.247.222.212:80', '112.95.205.49:8888', '61.184.109.33:61320', '211.103.198.106:8118', '139.199.201.82:8118', '140.143.170.222:8118', '218.28.58.150:53281', '115.46.70.47:8123', '115.46.74.184:8123', '58.251.49.4:43007', '222.94.146.107:3128', '115.219.104.210:8010', '115.46.72.126:8123', '116.228.53.234:43414', '111.225.8.62:9999', '182.92.113.183:8118', '182.88.134.89:8123', '112.95.205.122:9999', '123.180.71.27:8010', '116.7.176.75:8118', '115.210.64.224:8010', '27.202.138.75:9999', '182.88.160.111:8123', '59.78.35.129:1080', '115.151.7.188:808', '115.171.203.105:9000', '58.243.50.184:53281', '61.178.238.122:63000', '119.136.88.136:808', '115.46.79.167:9999', '115.46.79.51:8123', '115.46.71.97:8123', '115.151.4.111:808', '121.10.71.82:8118', '222.217.68.51:54355', '115.46.64.30:8123', '115.46.89.12:8123', '124.193.135.242:54219', '115.223.87.204:8010', '123.162.168.192:40274', '115.46.66.115:8123']

    return random.choice(pro)


def get_response(url):
    try:
        headers = randHeader()
        pro = randIp()
        response = requests.get(url,headers = headers,proxies={'http': pro})
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException as e:
        print(e,pro)
        return None

def parser_page(url,numbers,rate):
    global  review_nums
    # print(url)
    html = get_response(url)
    review_pat = re.compile('<div data-cid="(\d+)">',re.S)
    for num in re.findall(review_pat,html):
        # print(num)
        review_nums.append(num)
    next_pat = re.compile('<link rel="next" href="(.*?)"/>',re.S)
    next_url_part = re.findall(next_pat,html)[0]
    print(next_url_part)
    stop_url = '?rating={}&amp;start={}'.format(rate,numbers)
    if (next_url_part == stop_url ):
        return
    next_url = movie_url+next_url_part
    parser_page(next_url,numbers,rate)
    return


def get_content(num):
    file_path = "review-rating1.txt"
    content_url  = "https://movie.douban.com/j/review/{}/full".format(num)
    html=get_response(content_url)
    data = json.loads(html)
    soup = BeautifulSoup(data["body"],'lxml')
    content = soup.select('.review-content')[0].get_text()
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')


def main(n):
    print('the arg is :%s' % n)
    for num in review_nums[n*5:(n+1)*5]:
        get_content(num)


def start_with_thread():
    numbers = range(20)
    threads = []
    for i in numbers:
        threads.append(threading.Thread(target=main, args=(i,)))
        threads[i].start()
        time.sleep(random.randint(0,3)) # 暂停是为了防止并发数太多
    for i in numbers:
        threads[i].join()

review_nums = []
movie_url = 'https://movie.douban.com/subject/26752088/reviews'
url = 'https://movie.douban.com/subject/26752088/reviews?rating=1'
parser_page(url,100,1)
start_with_thread()