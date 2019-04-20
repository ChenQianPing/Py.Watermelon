# 箱线图
# 箱线图一般用来展现数据大小、占比、趋势等等的呈现，其包含一些统计学的均值、分位数、极值等等统计量，
# 因此，该图信息量较大，不仅能够分析不同类别数据平均水平差异（需在箱线图中加入均值点），还能揭示数据间离散程度、异常值、分布差异等等。
# 使用boxplot()方法绘制。

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(2)  # 设置随机种子
df = pd.DataFrame(np.random.rand(5,4),
columns=['A', 'B', 'C', 'D']) # 先生成0-1之间的5*4维度数据，再装入4列DataFrame中
df.boxplot() # 也可用plot.box()
plt.show()