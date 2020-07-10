import os
import random
import re
import pymysql
import requests
from bs4 import BeautifulSoup
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
        'Connection': head_connection[1],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header


def randIp():
    pro =['222.221.11.119:3128', '118.190.95.35:9001', '61.135.217.7:80', '183.47.40.35:8088', '111.230.183.90:8000', '61.138.33.20:808', '112.115.57.20:3128', '118.31.79.226:3128', '113.116.147.167:9000', '27.42.168.46:48919', '61.135.155.82:443', '60.205.142.252:8123', '125.121.138.136:808', '222.52.142.244:8080', '119.136.124.49:8118', '123.162.168.192:40274', '222.52.142.242:8080', '14.116.202.171:808', '58.251.234.159:9797', '121.10.71.82:8118', '115.46.67.173:8123', '218.14.115.211:3128', '171.38.42.81:8123', '58.251.234.149:9999', '219.238.186.188:8118', '221.237.146.165:8118', '183.16.20.235:8123', '110.72.47.129:8123', '175.155.24.35:808', '121.225.24.219:3128', '42.48.118.106:50038', '121.31.195.60:8123', '60.216.101.46:59351', '115.46.75.120:8123', '58.240.224.252:33035', '171.37.164.123:8123', '183.166.129.53:8080', '115.223.67.118:8010', '202.103.12.30:60850', '222.174.225.26:60984', '125.40.109.154:31610', '183.30.204.57:9999', '118.81.249.222:9797', '210.72.14.142:80', '175.148.79.171:1133', '180.168.113.204:1080', '171.37.152.174:8123', '115.223.79.174:8010', '122.115.78.240:38157', '183.172.128.119:8118', '171.39.73.92:8123', '171.38.91.187:8123', '222.186.45.123:62222', '175.155.24.3:808', '101.76.211.214:1080', '183.15.120.163:3128', '120.55.13.190:1080', '183.129.207.82:18118', '182.88.247.218:9797', '221.214.180.122:33190', '119.51.89.18:1080', '42.55.253.215:1133', '115.46.96.90:8123', '119.5.1.56:808', '121.69.37.6:9797', '112.95.206.68:9999', '117.85.85.249:53128', '115.46.68.11:8123', '14.221.165.68:9797', '180.175.136.195:54584', '115.46.76.40:8123', '111.72.154.240:53128', '115.46.78.138:8123', '111.160.236.84:39692', '118.213.182.194:47944', '124.235.181.175:80', '61.183.233.6:54896', '180.110.7.87:3128', '115.46.73.136:8123', '183.15.122.243:3128', '180.118.241.23:808', '114.112.84.197:39560', '60.191.134.165:9999', '118.25.177.45:1080', '58.87.73.43:8118', '123.180.69.178:8010', '124.173.72.50:80', '119.5.0.18:808', '118.81.251.4:9797', '111.72.154.231:53128', '115.46.71.197:8123', '115.46.75.91:8123', '121.31.176.109:8123', '115.46.99.187:8123', '121.31.192.47:8123', '221.7.255.167:8080', '116.228.53.234:43414', '115.46.65.31:8123', '115.46.78.33:8123', '183.15.120.152:3128']

    return random.choice(pro)

def db_conn_sql(sql):
    db = pymysql.connect("localhost", "root", "123456", "bookshopping")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("数据保存成功！")
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("数据保存失败！")
    # 关闭数据库连接
    db.close()

def save_to_img(url,root,path):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("图片保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


def get_response(url):
    try:

        headers = randHeader()
        pro = randIp()
        response = requests.get(url, headers=headers,proxies={'http': pro})
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            # print(response.status_code,pro)
            get_response(url)
    except RequestException as e:
        # print(e,pro)d
        get_response(url)

def get_urlList(html):
    soup = BeautifulSoup(html,'html.parser')
    all_list = []
    type_url_list  =soup.find_all(class_ = "tagCol")
    for item in type_url_list:
        part_list = item.select('a')
        all_list.append(part_list)
    # url_list = soup.select('.article .tagCol a')
    return  all_list

def get_book_urlList(url):
    html = get_response(url)
    url_pat = re.compile('<a class="nbg" href="(.*?)"',re.S)
    urlList = re.findall(url_pat,html)
    return urlList

def parse_book(url,one_type,two_type):
    html  = get_response(url)
    soup = BeautifulSoup(html,'html.parser')
    try:
        name_pat = re.compile('<span property="v:itemreviewed">(.*?)</span>', re.S)
        name = re.findall(name_pat, html)[0]
        img_pat = re.compile('<a class="nbg"\s+href="(.*?)" title=',re.S)
        img_url = re.findall(img_pat,html)[0]
        author_pat  = re.compile('<span class="pl">作者:</span>&nbsp;\s+<a href=".*?">(.*?)</a>',re.S)
        author = re.findall(author_pat,html)[0].replace('\n','').replace(' ','')
        pub_pat = re.compile('<span class="pl">出版社:</span>(.*?)<br/>', re.S)
        publisher = re.findall(pub_pat, html)[0].strip()
        date_pat = re.compile('<span class="pl">出版年:</span>(.*?)<br/>',re.S)
        date = re.findall(date_pat,html)[0].strip()
        price_pat = re.compile('<span class="pl">定价:</span>(.*?)<br/>',re.S)
        pri = re.findall(price_pat,html)[0].strip()
        price = re.findall(r'\d+\.?\d*',pri)[0]
        isbn_pat = re.compile('<span class="pl">ISBN:</span>(.*?)<br/>',re.S)
        isbn = re.findall(isbn_pat,html)[0].strip()
        intro = soup.select(".intro")[0].get_text()
        if len(intro) > 480:
            intro = intro[:480]+'...'

        number = random.randint(0, 1000)
        gphoto = isbn+'.jpg'
    except IndexError:
        return
    print(name,img_url,author,publisher,date,price,isbn)
    root = "C://Users//16474//Desktop//jsp程序设计//bookshoppingimage//"
    path = root + gphoto
    save_to_img(img_url,root,path)
    sql = "INSERT INTO books(gname,number, gphoto, one_type,two_type, producer,price,author,pdate,isbn,described)" \
          "VALUES ('%s','%d','%s','%s','%s','%s','%f','%s','%s','%s','%s')" \
          % (name, number, gphoto, one_type, two_type,publisher, float(price), author, date, isbn, intro)
    db_conn_sql(sql)





def main():
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    html = get_response(url)
    all_list = get_urlList(html)
    type_name = ["文学","流行","文化","生活","经管","科技"]
    count = 0
    # print(url_list)
    # item = url_list
    for type_url_list in all_list:
        one_type  = type_name[count]
        count = count+1
        print(one_type)
        for item in type_url_list:
            url = 'https://book.douban.com'+item['href']
            two_type = item.string
            print(two_type)
            for book_url in get_book_urlList(url):
                parse_book(book_url,one_type,two_type)
main()