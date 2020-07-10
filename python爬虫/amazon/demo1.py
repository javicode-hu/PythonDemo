"""爬取豆瓣网站的信息"""
import requests
from lxml import etree

# 请求头设置
headers = {
    "User-Agentv": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36",
    "Referer": "https://movie.douban.com/",
}

url = "https://movie.douban.com/cinema/nowplaying/chongqing/"
# 发起请求
rep = requests.get(url, headers=headers)
text = rep.text
# 转换成html格式
html = etree.HTML(text)
# 找到子孙节点ul标签
ul = html.xpath("//ul[@class='lists']")[0]
# 当前ul下的所有li标签
lis = ul.xpath("./li")
movies = []
# 循环每个li标签
for li in lis:
    # 直接@li标签的属性获取值
    title = li.xpath("@data-title")[0]
    print(title)
    score = li.xpath("@data-score")[0]
    print(score)
    region = li.xpath("@data-region")[0]
    print(region)
    actors = li.xpath("@data-actors")[0]
    print(actors)
    director = li.xpath("@data-director")[0]
    director
    liimg = li.xpath(".//img/@src")
    print(liimg)
    movie = {
        "title": title,
        "score": score,
        "region": region,
        "actors": actors,
        "director": director,
        "liimg": liimg,
    }
    movies.append(movie)