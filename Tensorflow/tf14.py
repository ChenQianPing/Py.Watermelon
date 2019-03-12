import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([105,109,119,120,120,120,121,121,121,123,123,123,123,124,125,125,125,126,126,126,126,126,127,127,127,127,127,129,130,130,130,131,131,131,132,132,132,132,132,133,134,134,134,136,136,137,137,142]) #身高
Yi=np.array([24,28,25,31,22,21,21,22,20,23,22,23,22,21,28,23,22,21,26,24,21,27,25,25,24,24,21,24,25,23,28,29,26,26,31,27,27,31,25,34,23,26,32,36,26,40,28,44])#体重

##需要拟合的函数func :指定函数的形状 k= 0.42116973935 b= -8.28830260655
def func(p,x):
    k,b=p
    return k*x+b

##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y

#k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0=[1,20]

#把error函数中除了p0以外的参数打包到args中(使用要求)
Para=leastsq(error,p0,args=(Xi,Yi))

#读取结果
k,b=Para[0]
print("k=",k,"b=",b)


#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="sample data",linewidth=2)

#画拟合直线
x=np.linspace(105,142,100) ##在105-142直接画100个连续点
y=k*x+b ##函数式
plt.plot(x,y,color="red",label="Fitting straight line",linewidth=2)
plt.legend() #绘制图例
plt.show()