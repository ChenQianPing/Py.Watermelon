#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

n = 6  # 6次投篮
p = 0.3 # 投中的概率
k = np.arange(0,6) # 随机变量X的值
print(k)
print("*"*20)
binomial = stats.binom.pmf(k,n,p)
print(binomial)

plt.plot(k, binomial, 'o-')
plt.title('binomial:n=%i,p=%.2f'%(n,p),fontsize=15)
plt.xlabel('number of success',fontproperties='SimHei')
plt.ylabel('probalility of success', fontsize=15)
# plt.grid(True)
plt.show()


