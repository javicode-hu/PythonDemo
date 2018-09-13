import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread  # 这是一个处理图像的函数

color_mask = imread('ben.jpg')

text = open('jay.txt','r',encoding='utf-8').read()
cut_text=jieba.cut(text)
result = ' '.join(cut_text)

# 生成词云图
wc =WordCloud(
    # 字体路径
    font_path="NotoSansHans-Medium.otf",
    # 背景颜色
    background_color='white',
    mask=color_mask,
    # 图片的宽
    width=500,
    # 图片的高
    height=350,
    # 字体大小
    max_font_size=50,
    # min_font_size=10,
)

wc=wc.generate(result)
print(type(wc))
# wc.to_file('wordcloud.png')

# 显示图片
# plt.figure('jay')
plt.imshow(wc)
plt.axis('off')
plt.show()



