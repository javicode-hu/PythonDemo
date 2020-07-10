import random
import threading
import time

import  requests
from requests import RequestException
from bs4 import BeautifulSoup
requests.adapters.DEFAULT_RETRIES = 5

#生成随机头
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
        'Connection': head_connection[1],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header

def randIp():
    pro =['116.4.11.54:9000', '1.196.160.101:9999', '61.135.217.7:80', '111.230.183.90:8000', '119.254.94.123:50972', '171.38.84.111:8123', '118.190.95.35:9001', '222.180.24.13:808', '114.249.116.203:9000', '113.116.59.172:9000', '112.115.57.20:3128', '218.22.102.107:80', '14.20.235.63:808', '115.219.108.245:8010', '171.37.167.200:8123', '125.46.0.62:53281', '180.213.180.58:8118', '58.53.128.83:3128', '221.214.180.122:33190', '114.94.141.100:1080', '171.37.165.180:8123', '171.37.165.70:8123', '124.235.181.175:80', '221.7.255.168:8080', '221.7.255.167:8080', '59.110.136.213:8080', '116.192.175.93:41944', '183.129.207.82:18118', '116.192.171.51:48565', '180.175.136.195:54584', '222.221.11.119:3128', '113.6.208.181:39097', '163.125.67.13:9797', '60.191.134.165:9999', '119.145.2.101:44129', '118.213.182.194:47944', '115.151.0.131:808', '61.176.223.7:58822', '101.251.216.103:8080', '218.14.115.211:3128', '60.216.101.46:59351', '118.178.227.171:80', '219.238.186.188:8118', '60.173.203.83:47300', '113.59.59.73:35683', '120.79.7.149:80', '42.48.118.106:50038', '123.162.168.192:40274', '171.212.91.95:61234', '118.181.226.216:36430', '114.113.126.86:80', '222.184.7.206:40908', '124.235.135.166:80', '114.112.84.197:39560', '123.207.110.28:3128', '119.29.174.35:1080', '222.52.142.242:8080', '180.106.16.118:3128', '110.40.13.5:80', '183.30.204.57:9999', '112.95.16.176:8088', '14.221.165.68:9797', '115.217.250.158:8123', '110.86.15.46:58945', '163.125.31.32:8118', '163.125.31.63:8118', '122.227.139.170:3128', '60.191.240.142:52780', '115.46.117.79:80', '115.46.75.39:8123', '218.17.253.106:60004', '175.148.69.162:1133', '218.85.200.204:53499', '115.46.70.6:8123', '49.65.39.84:8123', '175.155.24.48:808', '180.168.198.141:18118', '122.115.78.240:38157', '118.182.33.6:32559', '121.31.89.192:8123', '222.182.121.228:8118', '60.182.39.70:8010', '171.80.185.255:3128', '101.76.214.201:1080', '36.99.206.212:38551', '125.40.109.154:31610', '113.78.254.88:9000', '183.129.207.84:21231', '221.232.234.77:8010', '183.157.169.60:8118', '1.198.14.216:8010', '115.223.117.215:8010', '116.7.176.34:8118', '171.113.159.4:8010', '121.31.193.79:8123', '124.90.51.127:1080', '27.22.44.222:53281', '121.31.103.246:8123', '115.154.38.147:1080', '123.133.135.247:8118']

    return random.choice(pro)

def cookies_to_dict(cookies):
    items = cookies.split(';')
    d = {}
    for item in items:
        kv = item.split('=', 1)
        k = kv[0]
        v = kv[1]
        d[k] = v
    return d


def get_response(url):
    try:
        # cookies ='bid=SRbvGNrO76A; gr_user_id=7ea936d9-1a46-44aa-90b4-2a466f0e4bef; _vwo_uuid_v2=D58EFAF01B7AC2E9F661075F2AE409E59|fa5fbbc3c468d2d20693da39fddfd53c; ll="108304"; _ga=GA1.2.863171003.1541574569; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14897; ct=y; viewed="26698660_25862578_10594787_1186392"; ps=y; ue="1647431514@qq.com"; __utmc=30149280; dbcl2="148975015:XA6zfNKWS2s"; ck=yAAw; __utma=30149280.863171003.1541574569.1541767650.1541784728.11; __utmz=30149280.1541784728.11.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_douban=1; __utma=81379588.1943423650.1541574569.1541684825.1541784728.11; __utmc=81379588; __utmz=81379588.1541784728.11.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1541784728%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DkRcWYY-uCXnJSZAovYKbxqF4l8ZpdKbGALJToKschSaLWsoRg9c-J2YLn2ZVbk8I%26wd%3D%26eqid%3Daa1f43a000028650000000065be5c494%22%5D; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=789ed6e0-2240-438a-8235-4a1b145ff181; gr_cs1_789ed6e0-2240-438a-8235-4a1b145ff181=user_id%3A1; ap_v=0,6.0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_789ed6e0-2240-438a-8235-4a1b145ff181=true; _pk_id.100001.3ac3=a45c7a700a7da4f2.1541574569.10.1541784744.1541684825.; __utmb=30149280.5.10.1541784728; __utmb=81379588.5.10.154178472'
        # Cookies = cookies_to_dict(cookies)
        # headers = randHeader()
        # pro = randIp()
        kv = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        # response = requests.get(url, headers=headers,proxies={'http': pro},cookies = Cookies)
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            print(response.status_code,pro)
            get_response(url)
    except RequestException as e:
        print(e,pro)
        get_response(url)


def get_urlList(html):
    soup = BeautifulSoup(html,'html.parser')
    url_list = soup.select('.article .tagCol a')
    return  url_list

def parse_onepage_books(url):
    print(url)
    html  =get_response(url)
    soup = BeautifulSoup(html,'html.parser')

    for book_item in soup.select('.subject-item'):
        try:
            img = book_item.select('.nbg img')[0]['src']
            name = book_item.select('.info h2 a')[0]['title']
            info = book_item.select('.pub')[0].string.strip()
            score = book_item.select('.rating_nums')[0].string
            comments = book_item.select('.pl')[0].string.strip()
            introduce = book_item.find('p').text
        except AttributeError:
            introduce = ''
        except IndexError:
            score = '0'
        # print(img, name, info, score, comments, introduce)
        print(name)

    try:
        next = soup.select('.next a')[0]['href']
        nexturl = 'https://book.douban.com'+next
        parse_onepage_books(nexturl)
    except IndexError:
        return
def main():
    # global length
    # url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    # html = get_response(url)
    # print(html)
    # url_list = get_urlList(html)
    # # item = url_list
    # for item in url_list:
    #     url = 'https://book.douban.com'+item['href']
    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
    parse_onepage_books(url)
        # threading.currentThread(): 返回当前的线程变量。
        # print(threading.currentThread().getName())  # get/setName(name): 获取/设置线程名。
        # print('the arg is :%s' % n)
#
# def start_with_thread():
#     numbers = range(29)
#     threads = []
#     for i in numbers:
#         threads.append(threading.Thread(target=main, args=(i,)))
#         threads[i].start()
#         time.sleep(random.randint(0,3)) # 暂停是为了防止并发数太多
#     for i in numbers:
#         threads[i].join()
#
# start_with_thread()
main()