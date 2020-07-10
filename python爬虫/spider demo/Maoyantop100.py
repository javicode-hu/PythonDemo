import json
import  requests
from requests.exceptions import RequestException
import  re

def get_one_page(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        response = requests.get(url,headers = kv)
        if response.status_code ==200:
            return response.text
        return  None
    except RequestException:
        return None

    p = re.compile('<p class="name">.*?data-act="boarditem-click".*?>(.*?)</a>'
                   '</p>.*?<p class="star">\s+(.*?)\s+</p>.*?<p class="releasetime">(.*?)</p>', re.S)


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content,num):
    with open('第{}页.txt'.format(num),'w',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url ='http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        num = offset%10+1
        write_to_file(item,num)

if __name__ =='__main__':
    for i in range(10):
        main(i * 10)
        isGo = input("是否继续爬取？Y/N:")
        if isGo == "Y" or isGo =="y":
            continue
        else:
            print("爬取结束，谢谢！")
            break