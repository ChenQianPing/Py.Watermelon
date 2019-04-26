import numpy as np
import matplotlib.pyplot as plt

# 超几何分布 hypergeometric(ngood, nbad, nsample, size=None) 好的总数、坏的总数、每次采样数、试验次数
# np.random.hypergeometric(10,20,5,size=4)

# 在一个口袋中装有30个球，其中有10个红球，其余为白球，这些球除颜色外完全相同。游戏者一次从中摸出5个球。
# 摸到至少4个红球就中一等奖，那么获一等奖的概率是多少？
s = np.random.hypergeometric(10,20,5,size=1000000)
p = sum(s>=4)/1000000.
print(p)

fig = plt.figure(figsize=(8,6))
a1 = fig.add_subplot(2,2,1)

a1.hist(s ,bins=20,color='k',alpha=0.3)
plt.show()
