import random
import pymysql
import requests
from requests import RequestException
import  re
from bs4 import BeautifulSoup
import  os
import random


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
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return header

#源代码
def get_response(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        headers = randHeader()
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

#获取url
def get_page_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    url_pat = re.compile('<a class="a-link-normal a-text-normal" target="_blank" href="(.*?)">',re.S)
    urllist = re.findall(url_pat,html)
    url = set(urllist)
    return  url
    # urlList = soup.find_all('a',attrs={'class':'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'})
    # urlList = soup.select('.a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal')
    # print(urlList)


def db_conn_sql(sql):
    db = pymysql.connect("localhost", "root", "123456", "shopping")
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


#保存图片
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


def img_download(urlList,name):
    count = 1
    root = "C://Users//16474//Desktop//jsp程序设计//shoppingimage//"
    photo = []
    for url in urlList:
        path_name = name[:10]+str(count)+'.jpg'
        path =root+ path_name
        photo.append(path_name)
        # print(path)
        save_to_img(url,root,path)
        count = count+1
    return  '&'.join(photo)



def parser_one_page(url):
    html = get_response(url)
    # soup = BeautifulSoup(html, 'html.parser')
    # name = soup.find('span',attrs={'id':'productTitle'}).string
    name_pat = re.compile('<span id="productTitle" class="a-size-large">(.*?)</span>',re.S)
    name = re.findall(name_pat,html)[0]
    number = random.randint(0, 1000)
    img_pat = re.compile('{"mainUrl":"(.*?)"',re.S)
    img = re.findall(img_pat,html)
    # print(img)
    gphoto=img_download(img,name)
    types = "书籍"
    publisher_pat = re.compile('<li><b>出版社:</b>(.*?)</li>',re.S)
    publisher = re.findall(publisher_pat,html)[0]
    price_pat = re.compile('<span class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P">￥(.*?)</span>',re.S)
    price =float( re.findall(price_pat,html)[0])
    asin_pat = re.compile('<li><b>ASIN: </b>(.*?)</li>',re.S)
    asin = re.findall(asin_pat,html)[0]
    date_pat  =re.compile('<span class="a-size-medium a-color-secondary a-text-normal">(.*?)</span>',re.S)
    date = re.findall(date_pat,html)[-1].split(" ")[-1]
    # publish_date = re.search('\((.*?)\)',publisher[0]).group(0).strip('()')
    content_pat = re.compile('<noscript>\s+<div>(.*?)</div>',re.S)
    content = re.findall(content_pat,html)[0][:2000]
    carrige = float(random.randint(0,10))
    print("name",name)
    print("number",number)
    print("gphoto",gphoto)
    print("publisher",publisher)
    print("price",price)
    print(type(price))
    print("carrige",carrige)
    print(type(carrige))
    print("date",date)
    print("asin",asin)
    print("content",content)
    sql =  "INSERT INTO ymxgoods(gname,number, gphoto, types, producer,price,carriage,pdate,paddress,described)VALUES ('%s','%d','%s','%s','%s','%f','%f','%s','%s','%s')" % (name,number,gphoto,types,publisher,price,carrige,date,asin,content)
    db_conn_sql(sql)

def main():
    for i in range(10):
        url = 'https://www.amazon.cn/s/ref=sr_pg_1?rh=i%3Aaps%2Ck%3A%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&page={}&keywords=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&ie=UTF'.format(i+1)
        # url = "https://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D"
        print("第"+str(i+1)+"页")
        html = get_response(url)
        url_list=get_page_url(html)
        print(url_list)
        print(len(url_list))
        count = 0
        for url in url_list:
            try:
                count =count+1
                print(count)
                parser_one_page(url)
            except:
                continue


main()