from scipy.stats import binom  # 二项分布
from scipy.stats import expon # 指数分布
from scipy.stats import norm # 正态分布
from scipy.stats import poisson # 泊松分布
from scipy.stats import geom # 几何分布
from scipy.stats import hypergeom # 超几何分布
from scipy.stats import uniform  # 均匀分布

from scipy.stats import beta  # beta分布
from scipy.stats import f  # F分布
from scipy.stats import gamma  # gam分布
from scipy.stats import lognorm  # 对数正态分布
from scipy.stats import chi2  # 卡方分布
from scipy.stats import cauchy  # 柯西分布
from scipy.stats import laplace	  # 拉普拉斯分布
from scipy.stats import rayleigh	  # 瑞利分布
from scipy.stats import t	  # 学生T分布


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False


# 二项分布概率质量函数
# fig,ax = plt.subplots(1,1)
# n = 100
# p = 0.5
# #平均值, 方差, 偏度, 峰度
# mean,var,skew,kurt = binom.stats(n,p,moments='mvsk')
# print(mean,var,skew,kurt)
# #ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.arange(binom.ppf(0.01, n, p),binom.ppf(0.99, n, p))
# ax.plot(x, binom.pmf(x, n, p),'o')
# plt.title(u'二项分布概率质量函数')
# plt.show()

# 指数分布
# fig, ax = plt.subplots(1, 1)
#
# lambdaUse = 2
# loc = 0
# scale = 1.0 / lambdaUse
#
# # 平均值, 方差, 偏度, 峰度
# mean, var, skew, kurt = expon.stats(loc, scale, moments='mvsk')
# print(mean, var, skew, kurt)
# # ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.linspace(expon.ppf(0.01, loc, scale), expon.ppf(0.99, loc, scale), 100)
# ax.plot(x, expon.pdf(x, loc, scale), 'b-', label='expon')
#
# plt.title(u'指数分布概率密度函数')
# plt.show()

# 正态分布
# fig, ax = plt.subplots(1, 1)
#
# loc = 1
# scale = 2.0
# # 平均值, 方差, 偏度, 峰度
# mean, var, skew, kurt = norm.stats(loc, scale, moments='mvsk')
# print(mean, var, skew, kurt)
# # ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.linspace(norm.ppf(0.01, loc, scale), norm.ppf(0.99, loc, scale), 100)
# ax.plot(x, norm.pdf(x, loc, scale), 'b-', label='norm')
#
# plt.title(u'正太分布概率密度函数')
# plt.show()

# 泊松分布
# fig,ax = plt.subplots(1,1)
# mu = 2
# #平均值, 方差, 偏度, 峰度
# mean,var,skew,kurt = poisson.stats(mu,moments='mvsk')
# print(mean,var,skew,kurt)
# #ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.arange(poisson.ppf(0.01, mu),poisson.ppf(0.99, mu))
# ax.plot(x, poisson.pmf(x, mu),'o')
# plt.title(u'poisson分布概率质量函数')
# plt.show()

# 与二项分布对比
# fig, ax = plt.subplots(1, 1)
#
# n = 1000
# p = 0.1
# # 平均值, 方差, 偏度, 峰度
# mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
# print(mean, var, skew, kurt)
# # ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
# p1, = ax.plot(x, binom.pmf(x, n, p), 'b*', label='二项分布')
#
# mu = n * p
# # 平均值, 方差, 偏度, 峰度
# mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
# print(mean, var, skew, kurt)
#
# # ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
# p2, = ax.plot(x, poisson.pmf(x, mu), 'ro', label='泊松分布')
#
# plt.legend(handles=[p1, p2])
# plt.title(u'泊松分布与二项分布对比')
# plt.show()


# 几何分布
# fig,ax = plt.subplots(1,1)
# p = 0.5
# #平均值, 方差, 偏度, 峰度
# mean,var,skew,kurt = geom.stats(p,moments='mvsk')
# print(mean,var,skew,kurt)
# #ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
# x = np.arange(geom.ppf(0.01, p),geom.ppf(0.99, p))
# ax.plot(x, geom.pmf(x, p),'o')
# plt.title(u'几何分布概率质量函数')
# plt.show()


# 均匀分布
fig, ax = plt.subplots(1, 1)

loc = 1
scale = 1

# 平均值, 方差, 偏度, 峰度
mean, var, skew, kurt = uniform.stats(loc, scale, moments='mvsk')
print(mean, var, skew, kurt)
# ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
x = np.linspace(uniform.ppf(0.01, loc, scale), uniform.ppf(0.99, loc, scale), 100)
ax.plot(x, uniform.pdf(x, loc, scale), 'b-', label='uniform')

plt.title(u'均匀分布概率密度函数')
plt.show()