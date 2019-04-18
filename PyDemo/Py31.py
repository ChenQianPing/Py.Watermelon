from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import os
from PIL import Image
import matplotlib.pyplot as plt


# 人工去噪
excludes = {"将军","却说","荆州","二人","不可","于是","今日",\
            "不能","如此","主公","商议","如何","不敢","魏兵",\
            "军士","左右","军马","引兵","大喜","次日","天下","东吴","陛下","一人","都督","人马","不知","汉中","只见",\
            "众将","后主","蜀兵","上马","大叫","太守","此人","夫人","先主","后人","背后","城中","天子","一面","何不",\
            "大军","忽报","先生","百姓","何故","然后","先锋","不如","赶来","原来","令人","江东","下马","喊声","正是",\
            "徐州","忽然","因此","成都","不见","未知","大败","大事","之后","一军","引军","起兵","军中","接应","进兵",\
            "大惊","可以","以为","大怒","不得","心中","下文","一声","追赶","粮草"}

def get_text():
    f = open('threekingdoms.txt','r',encoding='utf-8').read()
    words = jieba.lcut(f)
    ls = []
    for i in words:
        if len(i)==1 or i in excludes:
            continue
        elif i in ['孟德','丞相']:
            ls.append('曹操')
        elif i in ['孔明曰','孔明','诸葛亮']:
            ls.append('诸葛亮')
        elif i in ['玄德曰', '玄德']:
            ls.append('刘备')
        elif i in ['关公', '云长','关公曰']:
            ls.append('关羽')
        elif i in ['都督']:
            ls.append('周瑜')
        else:
            ls.append(i)
    return ' '.join(ls)

def drawWordCloud(seg_list):
    '''
        制作词云
        设置词云参数
    '''
    color_mask = imread('bg.jpg')
    wc = WordCloud(
        #设置字体，不指定就会出现乱码，注意字体路径
        font_path="msyh.ttf",
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=200,
        #最大号字体
        max_font_size=60
    )
    wc.generate(seg_list) # 产生词云
    wc.to_file("ciyun.jpg") #保存图片

    img = Image.open('ciyun' + '.jpg')
    plt.figure("Image")  # 图像窗口名称
    plt.imshow(img)
    plt.axis('on')  # 关掉坐标轴为 off
    plt.title('image')  # 图像题目
    plt.show()


if __name__ == "__main__":
    txt = get_text()
    drawWordCloud(txt)

