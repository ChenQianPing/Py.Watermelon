# 柱状图和折线图混合使用
# 柱状图可以和折线图混合使用，用来表示某一个数据的变化趋势，下面是例子的柱状图表示水果的年度销量，折线图表示水果1月份的销量。

# 导入绘图模块
import matplotlib.pyplot as plt

jan_sales = [3010,4029,5021,3056]
# 构建数据
sales = [7125,12753,13143,8635]


# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['苹果','香蕉','梨','猕猴桃']

# 折线 1 x 2 y 3 color
plt.plot(x,jan_sales,'r')
# 4 line w
plt.plot(x,jan_sales,'g',lw=5)

# 绘图
plt.bar(range(4), sales, 0.4,color='b', alpha = 0.8)
# 添加轴标签
plt.ylabel('销量')
# 添加标题
plt.title('水果2018年度销量')
# 添加刻度标签
plt.xticks(range(4),['苹果','香蕉','梨','猕猴桃'])
# 设置Y轴的刻度范围
plt.ylim([2000,15000])

# 为每个条形图添加数值标签
for x,y in enumerate(sales):
    plt.text(x,y+100,'%s' %y,ha='center')

# 显示图形
plt.show()