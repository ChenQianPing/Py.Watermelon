
# 需求分析：实现对三国演义词频分析，统计出出场率高的前20位
# 1、读取文件内容。
# 2、进行分词。
# 3、对每个单词进行计数。
# 4、对单词的统计值从高到低进行排序。

import jieba
import wordcloud
from scipy.misc import imread

# 人工去噪
excludes = {"将军","却说","荆州","二人","不可","于是","今日",\
            "不能","如此","主公","商议","如何","不敢","魏兵",\
            "军士","左右","军马","引兵","大喜","次日","天下","东吴","陛下","一人","都督","人马","不知","汉中","只见",\
            "众将","后主","蜀兵","上马","大叫","太守","此人","夫人","先主","后人","背后","城中","天子","一面","何不",\
            "大军","忽报","先生","百姓","何故","然后","先锋","不如","赶来","原来","令人","江东","下马","喊声","正是",\
            "徐州","忽然","因此","成都","不见","未知","大败","大事","之后","一军","引军","起兵","军中","接应","进兵",\
            "大惊","可以","以为","大怒","不得","心中","下文","一声","追赶","粮草","丞相"}


txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)  # 精确模式：把文本精确地切分，不存在冗余

counts = {}
for word in words:
    if len(word) == 1:
          continue
    elif word == "诸葛亮" or word == "孔明曰" or word == "孔明":
        rword = "诸葛亮"
    elif word == "关公" or word == "云长" or word == '关公曰':
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
         rword = "刘备"
    elif word == "孟德":
         rword = "曹操"
    else:
         rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))


# def get_text():
#     f = open('threekingdoms.txt','r',encoding='utf-8').read()
#     words = jieba.lcut(f)
#     ls = []
#     for i in words:
#         if len(i)==1 or i in excludes:
#             continue
#         elif i in ['孟德','丞相']:
#             ls.append('曹操')
#         elif i in ['孔明曰','孔明','诸葛亮']:
#             ls.append('诸葛亮')
#         elif i in ['玄德曰', '玄德']:
#             ls.append('刘备')
#         elif i in ['关公', '云长','关公曰']:
#             ls.append('关羽')
#         elif i in ['都督']:
#             ls.append('周瑜')
#         else:
#             ls.append(i)
#     return ' '.join(ls)
#
#
# # 词云库
# # 加载形状图片要用到scipy库的imread方法
#
# img = imread('bg.jpg')
# txt = get_text()
# w = wordcloud.WordCloud(font_path='msyh.ttf',width=1000,height=500,background_color='white',mask=img)
# w.generate(txt)
# w.to_file('1.jpg')


