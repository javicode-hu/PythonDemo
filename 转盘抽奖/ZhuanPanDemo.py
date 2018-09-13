import threading
import tkinter

# 生成主窗口
import time

root = tkinter.Tk()
# 图形界面的标题
root.title('英雄联盟')
# 窗口的大小
root.minsize(300,300)
# 摆放按钮（按钮的位置和大小）
btn1 = tkinter.Button(root, text='盖伦', bg='red')
btn1.place(x=20, y=20,width=50, height=50)

btn2 = tkinter.Button(root, text='易大师', bg='white')
btn2.place(x=90, y=20,width=50, height=50)

btn3 = tkinter.Button(root, text='瑞文', bg='white')
btn3.place(x=160, y=20,width=50, height=50)

btn4 = tkinter.Button(root, text='维恩', bg='white')
btn4.place(x=230, y=20,width=50, height=50)

btn5 = tkinter.Button(root, text='诺克', bg='white')
btn5.place(x=230, y=90,width=50, height=50)

btn6 = tkinter.Button(root, text='亚索', bg='white')
btn6.place(x=230, y=160,width=50, height=50)

btn7 = tkinter.Button(root, text='安妮', bg='white')
btn7.place(x=230, y=230,width=50, height=50)

btn8 = tkinter.Button(root, text='提莫', bg='white')
btn8.place(x=160, y=230,width=50, height=50)

btn9 = tkinter.Button(root, text='李青', bg='white')
btn9.place(x=90, y=230,width=50, height=50)

btn10 = tkinter.Button(root, text='锤石', bg='white')
btn10.place(x=20, y=230,width=50, height=50)

btn11 = tkinter.Button(root, text='赵信', bg='white')
btn11.place(x=20, y=160,width=50, height=50)

btn12 = tkinter.Button(root, text='瑞兹', bg='white')
btn12.place(x=20, y=90,width=50, height=50)

# 将所有的选项放在列表中
herolist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]

# 定义标记，是否开启循环，开启为True
isloop = False

# 定义标记，是否停止，停止为True
stopsign = False

# 定义存储停止的id ，通过id的索引确定对应的选项
stopid = None

# 定义函数
def round():
    # global 声明全局变量
    global isloop
    global stopid
    # 判断是否开启循环
    if isloop == True:
        return
    i = 1
    # isinstance()判断一个对象是否是已知的类型
    if isinstance(stopid,int):
        i = stopid

    # 开始循环
    while True:
        # 延时操作
        time.sleep(0.03)
        for x in herolist:
            x['bg'] = 'white'

        herolist[i]['bg'] = 'red'

        i +=1;
        print('当前的i为：',i)

        # 如果i大于索引值直接归零
        if i>=len(herolist):
            i = 0
        if stopsign ==True:
            isloop = False
            stopid = i
            break

# 开始，停止
# 定义停止
def stoptask():
    global  stopsign
    if stopsign ==True:
        return
    stopsign = True
# 定义开始
def newtask():
    global stopsign
    global isloop

    stopsign = False

    # 建立线程
    t = threading.Thread(target=round)
    t.start()
    isloop = True

# 设置开始，停止按钮
btn_start  = tkinter.Button(root,text= '开始',command=newtask)
btn_start.place(x =90,y= 125,width =50,height= 50)
btn_stop = tkinter.Button(root,text='停止',command =stoptask)
btn_stop.place(x =160,y= 125,width =50,height= 50)

# 显示窗口
root.mainloop()