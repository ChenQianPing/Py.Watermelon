# 柱状图
# 只需绘制柱状图的函数bar()改成barh()就可以将柱状图长方形或长方体从垂直方向变为水平方向。
# 导入绘图模块
import matplotlib.pyplot as plt
# 构建数据
sales = [7125,12753,13143,8635]

# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['苹果','香蕉','梨','猕猴桃']
# 绘图
plt.barh(range(4), sales, 0.4,color='r', alpha = 0.8)
# 添加轴标签
plt.ylabel('销量')
# 添加标题
plt.title('水果2018年度销量')
# 添加刻度标签
plt.yticks(range(4),['苹果','香蕉','梨','猕猴桃'])
# 设置Y轴的刻度范围
plt.xlim([5000,15000])

# 为每个条形图添加数值标签
for x,y in enumerate(sales):
    plt.text(y+0.2,x,'%s' %y,va='center')

# 显示图形
plt.show()