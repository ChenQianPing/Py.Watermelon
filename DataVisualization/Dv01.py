# 柱状图
# 导入绘图模块
import matplotlib.pyplot as plt
# 构建数据
sales = [7125,12753,13143,8635]

# 中文乱码的处理，rcParams也可以用于设置图的分辨率，大小等信息
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图,第一个参数是x轴的数据，第二个参数是y轴的数据，第三个参数是柱子的大小，默认值是1（值在0到1之间），color是柱子的颜色，alpha是柱子的透明度
plt.bar(range(4), sales, 0.4,color='r', alpha = 0.8)
# 添加轴标签
plt.ylabel('销量')
# 添加标题
plt.title('水果2018年度销量')
# 添加刻度标签
plt.xticks(range(4),['苹果','香蕉','梨','猕猴桃'])
# 设置Y轴的刻度范围
plt.ylim([5000,15000])

# 为每个条形图添加数值标签
for x,y in enumerate(sales):
    plt.text(x,y+100,'%s' %y,ha='center')

# 显示图形
plt.show()