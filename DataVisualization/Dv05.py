# 饼图
# 饼图主要是用来表示数据的占比，给人一眼就可以看出数据的占比大小。饼图使用pie()函数绘制。

import matplotlib.pyplot as plt

# 设置绘图的主题风格（不妨使用R中的ggplot分隔）
plt.style.use('ggplot')

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['苹果','香蕉','梨','猕猴桃','桔子']

explode = [0,0.1,0,0,0] # 用于突出显示大专学历人群
colors=['#FEB748','#EDD25D','#FE4F54','#51B4FF','#dd5555'] # 自定义颜色

# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)

# 绘制饼图
plt.pie(x = edu,# 绘图数据
    explode=explode, # 突出显示香蕉人群
    labels=labels, # 添加水果销量水平标签
    colors=colors, # 设置饼图的自定义填充色
    autopct='%.1f%%', # 设置百分比的格式，这里保留一位小数
    pctdistance=0.8,# 设置百分比标签与圆心的距离
    labeldistance = 1.15, # 设置销量水平标签与圆心的距离
    startangle = 180, # 设置饼图的初始角度
    radius = 1.5, # 设置饼图的半径
    counterclock = False, # 是否逆时针，这里设置为顺时针方向
    wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
    textprops = {'fontsize':12, 'color':'k'}, # 设置文本标签的属性值
    center = (1.8,1.8), # 设置饼图的原点
    frame = 1)# 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('2018年水果销量分析')

# 显示图形
plt.show()


# 简单介绍下pie函数参数：
# x: 指定绘图的数据
# explode:指定饼图某些部分的突出显示，即呈现爆炸式
# labels：为饼图添加标签说明，类似于图例说明
# colors：指定饼图的填充色
# autopct：设置百分比格式，如'%.1f%%'为保留一位小数
# shadow：是否添加饼图的阴影效果
# pctdistance:设置百分比标签与圆心的距离
# labeldistance：设置各扇形标签（图例）与圆心的距离；
# startangle：设置饼图的初始摆放角度, 180为水平；
# radius：设置饼图的半径大小；
# counterclock：是否让饼图按逆时针顺序呈现, True / False；
# wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等, 如wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}
# textprops：设置饼图中文本的属性，如字体大小、颜色等；
# center：指定饼图的中心点位置，默认为原点
# frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；