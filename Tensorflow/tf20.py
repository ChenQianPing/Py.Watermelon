import numpy as np
import matplotlib.pyplot as plt

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi=np.array([105,109,119,120,120,120,121,121,121,123,123,123,123,124,125,125,125,126,126,126,126,126,127,127,127,127,127,129,130,130,130,131,131,131,132,132,132,132,132,133,134,134,134,136,136,137,137,142]) #身高
Yi=np.array([24,28,25,31,22,21,21,22,20,23,22,23,22,21,28,23,22,21,26,24,21,27,25,25,24,24,21,24,25,23,28,29,26,26,31,27,27,31,25,34,23,26,32,36,26,40,28,44])#体重
xy_res = []


##计算残差
def residual(x, y):
    res = y - (x ** 0.860357336936 - 19.6659389666)
    return res


##读取残差
for d in range(0, len(Xi)):
    res = residual(Xi[d], Yi[d])
    xy_res.append(res)
##print(xy_res)
##计算残差平方和:22.881076636 -->越小拟合情况越好
xy_res_sum = np.dot(xy_res, xy_res)
# print(xy_res_sum)

'''
      标准残差:  （残差-残差平均值）/残差的标准差
'''
##计算残差平均值
xy_res_avg = 0
for d in range(0, len(xy_res)):
    xy_res_avg += xy_res[d]

xy_res_avg /= len(xy_res)

# 残差的标准差
xy_res_sd = np.sqrt(xy_res_sum / len(Xi))

##标准化残差
xy_res_sds = []

for d in range(0, len(Xi)):
    res = (xy_res[d] - xy_res_avg) / xy_res_sd
    xy_res_sds.append(res)

print(xy_res_sds)

# 标准化残差分布
plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
plt.scatter(Xi, xy_res_sds)
plt.show()

'''
  1.绝大部分数据分布在(-2,+2)的水平带状区间内，因此模型拟合较充分
  2.数据点分布稍均匀，但没有达到随机均匀分布的状态。此外，部分数据点还呈现某种曲线波动形状，
    有少许系统性偏差。因此可能采用非线性拟合效果会更好
'''