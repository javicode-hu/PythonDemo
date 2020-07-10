import requests


def getHTMLText(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()  # 如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == '__main__':
    url = "https://book.douban.com/"
    print(getHTMLText(url))
