import numpy as np
import scipy.stats as stats
import pylab

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([105,109,119,120,120,120,121,121,121,123,123,123,123,124,125,125,125,126,126,126,126,126,127,127,127,127,127,129,130,130,130,131,131,131,132,132,132,132,132,133,134,134,134,136,136,137,137,142]) #身高
Yi=np.array([24,28,25,31,22,21,21,22,20,23,22,23,22,21,28,23,22,21,26,24,21,27,25,25,24,24,21,24,25,23,28,29,26,26,31,27,27,31,25,34,23,26,32,36,26,40,28,44])#体重
xy_res=[]

##计算残差
def residual(x,y):
    res=y-(0.42116973935*x-8.28830260655)
    return res

##读取残差
for d in range(0,len(Xi)):
    res=residual(Xi[d],Yi[d])
    xy_res.append(res)
##print(xy_res)

##计算残差平方和:22.8833439288 -->越小拟合情况越好
xy_res_sum=np.dot(xy_res,xy_res)
#print(xy_res_sum)

##如果数据拟合模型效果好，残差应该遵从正态分布(0,d*d:这里d表示残差)
#画样本点
stats.probplot(np.array(xy_res),dist="norm",plot=pylab)
pylab.show()