from wordcloud import WordCloud                                            #导入matplotlib作图的包
import matplotlib.pyplot as plt                                            #读取文件,返回一个字符串，使用utf-8编码方式读取
import jieba
from scipy.misc import imread

f = open('E:\物联网安全\scrapy\comments.txt','r',encoding='utf-8').read()        #生成一个词云对象
ct = ','.join(jieba.cut(f,cut_all = True))                                     # 分词处理

bpg=imread('E:\ee\cloud_analyze\gp.png')                                       # 读取图片文件，用于词云mask
wordcloud = WordCloud(
        font_path='C:/Users/Windows/fonts/simkai.ttf',
        background_color="white",                                        #设置背景为白色，默认为黑色
        width=1500,                                                        #设置图片的宽度
        height=960,                                                        #设置图片的高度
        margin=10,                                                           #设置图片的边缘
        mask =bpg
        ).generate(ct)                                     # 绘制图片
plt.imshow(wordcloud)                                       # 消除坐标轴
plt.axis("off")                                             # 展示图片
plt.show()                                                   # 保存图片
wordcloud.to_file('my_test2.png')
