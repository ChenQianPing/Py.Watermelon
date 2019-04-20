# 雷达图
# 雷达图可以用来显示一个周期数值的变化，也可以用来展示对个对象/维度之间的关系

import numpy as np
import matplotlib.pyplot as plt

#标签
labels = np.array(['语文','数学','英语','生物','物理','化学'])
#数据个数
dataLenth = 6
#数据
data = np.array([7,4,3,6,4,8])

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数！！
ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("matplotlib雷达图", va='bottom', fontproperties="SimHei")
ax.set_rlim(0,10)
ax.grid(True)
plt.show()