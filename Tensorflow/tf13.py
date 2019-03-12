import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([105,109,119,120,120,120,121,121,121,123,123,123,123,124,125,125,125,126,126,126,126,126,127,127,127,127,127,129,130,130,130,131,131,131,132,132,132,132,132,133,134,134,134,136,136,137,137,142]) #身高
Yi=np.array([24,28,25,31,22,21,21,22,20,23,22,23,22,21,28,23,22,21,26,24,21,27,25,25,24,24,21,24,25,23,28,29,26,26,31,27,27,31,25,34,23,26,32,36,26,40,28,44])#体重

#画样本点
plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
plt.scatter(Xi,Yi,color="green",label="sample data",linewidth=1)
plt.show()