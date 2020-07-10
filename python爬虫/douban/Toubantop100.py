import json
import  os
import  requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code ==200:
            response.encoding = response.apparent_encoding
            return response.text
        return  None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<a.*?nbg.*?src="(.*?)".*?width="75".*?alt="(.*?)".*?class=""/>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'image':item[0],
            'name':item[1]
        }
def write_to_file(content):
    with open('douban.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
def save_all_img(url,root,fpath):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(fpath):
            r = requests.get(url)
            with open(fpath, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")





def main():
    url = 'https://movie.douban.com/chart'
    html = get_one_page(url)

    for item in parse_one_page(html):
        root = "F://doubantop//"
        url = item['image']
        path = root+item['name']+'.jpg'

        print(item)
        save_all_img(url,root,path)
        write_to_file(item)


main()