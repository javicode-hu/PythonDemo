from aip import AipOcr
import  io
import tkinter.filedialog
from tkinter.filedialog import *
from PIL import  Image,ImageTk

fname = ""  # 选择的图片文件路径


def resize(w, h, w_box, h_box, pil_image):   # 缩放图片适应控件
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def select_file():
    global fname
    default_dir = r"C:\Users\Administrator.ZNQBQGNSV4CXCTK\Desktop"  # 设置默认打开目录
    fname = tkinter.filedialog.askopenfilename(title=u"选择文件",initialdir=(os.path.expanduser(default_dir)))
    filepath = StringVar()
    filepath.set(fname)
    Entry(root, textvariable=filepath, width=60).grid(row=0, column=1, padx=4)
    w_box = 600
    h_box = 600
    pil_image = Image.open(fname)
    # 获取图像的原始大小
    w, h = pil_image.size
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    bm = ImageTk.PhotoImage(pil_image_resized)
    label2 = Label(root, image=bm)
    label2.bm = bm
    label2



def trans_word():
    global fname
    APP_ID = 'baeapp-y4zd6wmjjwbm'

    API_KEY = '21927f7f0726419ca4e1809e5db52b2c'

    SECRET_KEY = 'c6e1c53f5fe64f2b84c7e15a9d38eb2c'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    word=""
    with open(fname,'rb') as f:
        img = f.read()
        msg = client.basicAccurate(img)
        for i in msg.get('words_result'):
            word = word+i.get('words')+'\n'
            # print(i.get('words'))
    # getword = StringVar()
    # getword.set(word)
    S = Scrollbar(root)

    T=Text(root,font=('微软雅黑',10))
    T.grid(row=4,columnspan=3)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,word)


root = Tk()
root.title('人工智能文字识别')
root.geometry('800x800')# 坐标，大小

Label(root,text= '图片:').grid(row=0,column=0)
Label(root,text='显示图片:').grid(row=1,column=0)
Label(root,text='识别文字:').grid(row=3,column=0)
Entry(root,width=60).grid(row=0, column=1,padx=4)
Button(root,text='选择图片',command=select_file).grid(row=0, column=2,padx=4)
Button(root,text='开始识别',command=trans_word).grid(row=0, column=3,padx=4)

# print tkFileDialog.askdirectory()  # 返回目录路径
# fd = LoadFileDialog(root)  # 创建打开文件对话框
# filename = fd.go()  # 显示打开文件对话框，并获取选择的文件名称
# print(filename)





root.mainloop()