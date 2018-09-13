import tkinter.filedialog
from tkinter.filedialog import *
from PIL import  Image,ImageTk
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud,  ImageColorGenerator, wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import  tkinter.messagebox
import os

global img_name,data_name,h1,wc,Iswc
Iswc = False

def resize(w, h, w_box, h_box, pil_image):   # 缩放图片适应控件
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)

def select_data():
    default_dir = r"F:\python 项目\词云数据展示"  # 设置默认打开目录
    global data_name
    data_name = tkinter.filedialog.askopenfilename(title=u"选择文本文件", initialdir=(os.path.expanduser(default_dir)))
    if data_name[-3:] != 'txt':
        tkinter.messagebox.showinfo('警告', '请选择文本文件')
        return select_data()
    filepath = StringVar()
    filepath.set(data_name)
    T1.delete(0,END)
    T1.insert(0, data_name)

def select_img():
    name = T1.get()
    if not name:
        tkinter.messagebox.showinfo('警告', '请先选择文本继续')
        return
    global img_name
    img_name = tkinter.filedialog.askopenfilename(title=u"选择图片文件", initialdir=(os.path.expanduser(data_name)))
    if img_name[-3:] not in ['jpg','png','jpeg','gif']:
        tkinter.messagebox.showinfo('警告', '请选择图片文件')
        return select_img()
    filepath = StringVar()
    filepath.set(img_name)
    T2.delete(0,END)
    T2.insert(0, img_name)
    w_box = 400
    h_box = 400
    pil_image = Image.open(img_name)
    # 获取图像的原始大小
    w, h = pil_image.size
    print(w,h)
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    global h1
    w1, h1 = pil_image_resized.size
    print(w1,h1)
    bm = ImageTk.PhotoImage(pil_image_resized)
    Label(root, text='原图:').place(x=10, y=125)
    L1 = Label(root, image=bm,width=400,height=275)
    L1.bm = bm
    L1.place(x=100, y=125)

def create_wc():
    global Iswc
    Iswc = True
    t1_name = T1.get()
    t2_name = T2.get()
    if not (t1_name and t2_name):
        tkinter.messagebox.showinfo('警告', '无法生成词云图，请先选择数据继续')
        return
    color_mask = imread(img_name)  # 解析该图片
    image_colors = ImageColorGenerator(color_mask)
    global wc
    wc = WordCloud(
               background_color='white',  # 背景颜色
               max_words=5000,  # 最大词数
               mask=color_mask,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=40,  # 显示字体的最大值
               # stopwords=STOPWORDS.add(''),  # 使用内置的屏蔽词，再添加'苟利国'
               font_path="NotoSansHans-Medium.otf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               color_func=image_colors,
               # random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
                   )
    text = open(data_name, 'r', encoding='utf-8').read()
    cut_text = jieba.cut(text)
    result = ' '.join(cut_text)
    wc.generate(result)
    wc.to_file('demo.png')
    # print(type(wc))
    w_box = 400
    h_box = 400
    pil_image = Image.open('demo.png')
    # 获取图像的原始大小
    w, h = pil_image.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    # w1, h1 = pil_image_resized.size
    bm = ImageTk.PhotoImage(pil_image_resized)
    Label(root, text='词云图:').place(x=10, y=135+275)
    L2 = Label(root, image=bm,width=400,height=275)
    L2.bm = bm
    L2.place(x=100, y=135+275)
    if os.path.exists('demo.png'):
        # 删除文件，可使用以下两种方法。
        os.remove('demo.png')
        # os.unlink(my_file)
def save_wc():
    t1_name = T1.get()
    t2_name = T2.get()
    if not (t1_name and t2_name):
        tkinter.messagebox.showinfo('警告', '无法保存，请先选择数据继续')
        return
    options = {}
    options['defaultextension'] = ".png"
    options['filetypes'] = (("png files", ".png"), ("All files", "*"))
    options['initialdir'] = os.path.expanduser(r"F:\python 项目\词云数据展示")
    options['initialfile'] = ""
    options['title'] = u"选择文件夹"
    if Iswc:
        outfile = tkinter.filedialog.asksaveasfilename(**options)
        if  outfile:
            wc.to_file(outfile)
            tkinter.messagebox.showinfo('提示','保存成功！')
    else:
        tkinter.messagebox.showinfo('警告', '无法保存，请先生成词云图')
        return




def reselect():
    select_data()
    select_img()



root = Tk()
root.title('词云图生成器')
root.geometry('700x700')# 坐标，大小
root.resizable(width=False,height=True)
# s1 = Scrollbar(root,orient=VERTICAL)#orient默认为纵向
# s1.pack(fill=Y, side=RIGHT)
# s1.set(0.5,1)
Label(root,text= '选择数据:').place(x=10,y=10)
Label(root,text= '选择图云背景:').place(x=10,y=45)
T1=Entry(root,width=60)
T1.place(x=100, y=10)
T2=Entry(root,width=60)
T2.place(x=100,y=45)
Button(root,text='浏览',command=select_data).place(x=550,y=5,width=60)
Button(root,text='浏览',command=select_img).place(x=550,y=40,width=60)
Button(root,text='开始生成',command=create_wc).place(x=20,y=80,width=60)
Button(root,text='保存词云图',command=save_wc).place(x=100,y=80,width=100)
Button(root,text='重新选择',command=reselect).place(x=550,y=80,width=60)


root.mainloop()