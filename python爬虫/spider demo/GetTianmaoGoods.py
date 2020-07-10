import  requests
from requests import RequestException
import  re
from bs4 import BeautifulSoup

import json

def get_price(url):
    sku = url.split('/')[-1].strip(".html")
    price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku
    response  =get_response(price_url)
    result = json.loads(response)
    price = result[0]['p']
    print(price)
    return price

def get_response(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None

def get_onepage_url(html):
    pattern = re.compile('<li data-sku="(.*?)" class="gl-item">',re.S)
    url_list = re.findall(pattern, html)

    return url_list

def get_goods_info(url):

    html = get_response(url)
    soup = BeautifulSoup(html,'html.parser')
    imgInfo = soup.find('ul',attrs={'class':'lh'})
    img_urlList = imgInfo.find_all('img')
    for img_url in img_urlList:
        print(img_url['src'])
    name = soup.find('div',attrs={'class':'sku-name'}).string.strip()
    print(name)
    get_price(url)
    goodInfo = soup.select('.p-parameter-list li');
    publisher = goodInfo[1]['title']
    date = goodInfo[4]['title']
    print(publisher,date)
    



def db_conn():
    pass

keywords  ="编程书籍"
url="https://search.jd.com/Search?keyword=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&page=1&s=1&click=0	"
html = get_response(url)
get_onepage_url(html)

get_goods_info('https://item.jd.com/26147900526.html')