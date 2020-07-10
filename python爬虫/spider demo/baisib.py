# coding:utf-8
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import  urllib.request
import requests
from bs4 import  BeautifulSoup
import  sys
import  os
# sys.setdefaultencoding('utf-8') #输出格式

urlList = []
a = 1 #页数

def get():
    global  a
    kv = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://www.budejie.com/video/'+str(a)
    varl.set('已经获取到第%s页的视频'%(a))
    response = requests.get(url,headers=kv)
    html =response.text
    a+=1
    soup = BeautifulSoup(html, "html.parser")
    cont = soup.select(".j-r-list-c")

    for item in cont:
        name = item.find('a').text
        pmUrl = item.select(' .j-video')[0].get('data-mp4')
        # 以元祖的形式添加到数组
        urlList.append((name, pmUrl))
    return urlList

id =1 #视频个数
def write():
    global  id
    while id<10:
        url_name = get()
        for item in url_name:
            urllib.request.urlretrieve(item[1], 'video\\%s.mp4' % (item[0]))
            text.insert(END,str(id)+'.'+item[1]+'\n'+item[0]+'\n')
            url_name.pop(0)  # 删除已经有的
            id +=1
    varl.set('视频抓取完毕！')

def start():
    thr = threading.Thread(target=write)
    thr.start()

root  = Tk()
root.title('视频爬取1.0')
#root.geometry('500x300')# 坐标，大小
text = ScrolledText(root,font=('微软雅黑', 10)) # 文本滚动条
text.grid()
button = Button(root,text='开始爬取',font=('微软雅黑',10),command=start) # 按钮控件
button.grid()
varl = StringVar()
label = Label(root,font=('微软雅黑', 10),fg='red',textvariable = varl)
label.grid()
varl.set('熊猫已准备')
root.mainloop()