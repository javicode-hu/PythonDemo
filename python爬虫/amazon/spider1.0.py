"""爬取腾讯招聘网找工作"""
import requests
from lxml import etree

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36",
           "Referer": "https://hr.tencent.com/position.php?keywords=python&lid=2218&tid=87&start=0"
           }
BASE_URL = "https://hr.tencent.com/"


def get_detail_urls(url):
    rep = requests.get(url=url, headers=HEADERS)
    html = etree.HTML(rep.text)
    detail_urls = html.xpath("//table//td[@class='l square']/a/@href")
    detail_urls = map(lambda url: BASE_URL+url, detail_urls)
    return detail_urls


def get_parse_detail(url):
    job_offers = {}
    res = requests.get(url=url, headers=HEADERS)
    html = etree.HTML(res.text)
    position = html.xpath("//table//td[@class='l2 bold size16']/text()")[0]
    job_offers["position"] = position
    tds = html.xpath("//table//tr[@class='c bottomline']/td/text()")
    for i in range(len(tds)):
        job_offers["location"] = tds[0]
        job_offers["category"] = tds[1]
        job_offers["recruits"] = tds[2]
    duties = html.xpath("//tr[3][contains(@class, 'c')]//li/text()")
    job_offers["duties"] = duties
    claim = html.xpath("//tr[4][contains(@class, 'c')]//li/text()")
    job_offers["claim"] = claim
    return job_offers


def spider():
    base_url = "https://hr.tencent.com/position.php?keywords=python&lid=2218&tid=87&start={}#a"
    squres = []
    for i in range(0, 340, 10):
        url = base_url.format(i)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            squre = get_parse_detail(detail_url)
            squres.append(squre)
            print(squre)


if __name__ == '__main__':
    spider()