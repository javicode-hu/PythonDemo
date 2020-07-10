import os
import requests
from requests import RequestException
import  re
import sys



#获取网页源代码
def get_response(isbn):
    url = "https://douban.uieee.com/v2/book/isbn/{}".format(isbn)
    try:
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.get(url, headers=kv)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        return None
    except RequestException:
        return None
#提取图书信息
def get_book_url(html):
    root = "C://Users//16474//Desktop//数据库//"
    name_pat = re.compile('"isbn13":".*?","title":"(.*?)","url"',re.S)
    name = re.findall(name_pat,html)[0]
    author_pat = re.compile('"author":\["(.*?)"\]',re.S)
    author = re.findall(author_pat,html)[0]
    press_pat = re.compile('"publisher":"(.*?)"',re.S)
    press = re.findall(press_pat,html)[0]
    date_pat  =re.compile('"pubdate":"(.*?)"',re.S)
    date = re.findall(date_pat,html)[0]
    isbn_pat = re.compile('"isbn13":"(.*?)"',re.S)
    isbn = re.findall(isbn_pat,html)[0]
    price_pat = re.compile('"price":".*?(-?\d+\.?\d*e?-?\d*?).*?"',re.S)
    price = re.findall(price_pat,html)[0]
    brief_pat =re.compile('"summary":"(.*?)"',re.S)
    brief = re.findall(brief_pat,html)[0].replace('\\n','')
    photo_pat = re.compile('"medium":"https://(.*?).doubanio.com\\\/view\\\/subject\\\/m\\\/public\\\/(.*?)"',re.S)
    photo = re.findall(photo_pat,html)[0]
    path = root +photo[1]
    save_to_img(photo,root,path)
    print(name)
    print(author)
    print(press)
    print(date)
    print(isbn)
    print(price)
    print(brief)
    # print(photo)
    print(path)

def save_to_img(photo,root,path):
    url  = "https://{}.doubanio.com/view/subject/l/public/{}".format(photo[0],photo[1])
    # print(url)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                # print("图片保存成功")
        else:
            pass
            # print("文件已存在")
    except:
        pass
        # print("爬取失败")



if __name__ == '__main__':
    # isbn  =sys.argv[1]
    isbn =  "9787542668844"
    # print(isbn)
    html = get_response(isbn)
    # print(html)
    get_book_url(html)

