# 气泡图
# # 气泡图用于判断3个变量之间是否存在某种关系。它跟散点图有点类似，只不过气泡图以气泡大小作为新的维度

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

d = {"时间":pd.Series([2006,2007,2008,2009,2010]),
     "数量":pd.Series([10,200,120,150,300]),
     "大小":pd.Series([50,130,40,50,160]),
     "分类":pd.Series([1,2,0,1,2]),
     "判断":pd.Series([True,True,True,True,True])}

df=pd.DataFrame(d)

#先定义气泡大小，rank 函数将大小列进行大小分配，越大的值分配结果也越高
#n 为倍数，用来调节气泡的大小，且看后头

size=df['大小'].rank()
n=20

#定义一个字典，将颜色跟对应的分类进行绑定

color={0:'red',1:'blue',2:'orange'}

#增加color的参数，用列表解析式将data分类中的每个数据的数字映射到前面color的颜色中

plt.scatter(df['数量'],df['大小'],color=[color[i] for i in df['分类']],s=size*n,alpha=0.6)
plt.show()