import requests

jar = requests.cookies.RequestsCookieJar()
jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
jar.set('11', '25678', domain='.douban.com', path='/')
url = 'https://book.douban.com/people/122624856/collect'
r = requests.get(url, cookies=jar)
print(r.text)
