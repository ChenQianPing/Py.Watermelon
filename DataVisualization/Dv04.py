# 折线图
# 折线图主要用于表示数据变化的趋势。折线图是直线将不同的点连接起来。

# 导入绘图模块
import matplotlib.pyplot as plt

# 构建数据
jan_sales = [3010,4029,5021,3056]


# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['苹果','香蕉','梨','猕猴桃']

# 第一个参数是x轴，第二参数时y轴数据，第三个参数是线的颜色，第二个参数是线条的粗细
# 4 line w
plt.plot(x,jan_sales,'r',lw=5)

# 添加标题
plt.title('水果2018年度1月份销量图')
plt.ylim([2000,15000])

# 为每个点添加数值标签
for x,y in enumerate(jan_sales):
    plt.text(x,y+100,'%s' %y,ha='center')

# 显示图形
plt.show()