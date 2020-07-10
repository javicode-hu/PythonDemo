import requests
from requests import RequestException
import re
import  os
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
    pattern = re.compile('<a.*?data-original=".*?id=(\d+).*?userid=(\d+).*?".*?/></a>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'url_1':item[1],
            'url_2':item[0]
        }

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

def main():
    url = 'http://www.meisupic.com/searchi.php?s_keyword=%E8%87%AA%E7%84%B6&offset=&sort=4&phototype=&orientation=&people_only=&race=&age=&gender=&quantity=&color=&categories=&username=&exclude_keyword=&image_url=&editorial=&keyword=%E8%87%AA%E7%84%B6'
    html = get_one_page(url)

    for item in parse_one_page(html):
        root = "F://huaban//"
        url = 'http://meisupic.oss-cn-beijing.aliyuncs.com/thumbs/'+item['url_1']+'/'+item['url_2']+'/'+'api_thumb_450.jpg'
        path = root +item['url_1']+item['url_2']+'.jpg'
        save_to_img(url,root,path)

main()