# -*- coding:utf-8 -*-
from tkinter import  *
import  tkinter.messagebox
from PIL import  Image,ImageTk
import  requests
import re
import  os

def get_img():
    name = nameent.get()
    if not name:
        tkinter.messagebox.showinfo('警告','请输入名字再继续')
        return
    data = {
        'word': name,
        'sizes': '60',
        'fonts': 'jfcs.ttf',
        'fontcolor': '#000000'
    }
    url= 'http://www.uustv.com/'
    result = requests.post(url, data=data)
    result.encoding = 'utf-8'
    pattern = re.compile('<div class="tu">﻿<img src="(.*?)"/></div>')
    imgurl =url + (re.findall(pattern,result.text)[0])
    response = requests.get(imgurl).content
    Root = "F://QianPic//"
    path = Root +'{}.gif'.format(name)
    if not os.path.exists(Root):
        os.mkdir(Root)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(response)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
    # with open('{}.gif'.format(name),'wb') as f:
    #     f.write(response)
    # try:
    #     im = Image.open('{}.gif'.format(name))
    #     im.show()
    #     im.close()
    # except:
    #     print('请自己打开！')
    bm = ImageTk.PhotoImage(file='F://QianPic//{}.gif'.format(name))
    label2 = Label(root,image =bm)
    label2.bm = bm
    label2.grid(row=2,columnspan=3)
root = Tk()
root.title('python签名设计')
root.geometry('600x300')# 坐标，大小
Label(root,text="姓名：",font=('微软雅黑',15)).grid()
nameent = Entry(root,font=('微软雅黑',15))
nameent.grid(row=0, column=1)
button = Button(root,text='一键设计签名',font=('微软雅黑',15),width ='15',height='1',command=get_img) # 按钮控件
button.grid(row=0,column=2)
mainloop()