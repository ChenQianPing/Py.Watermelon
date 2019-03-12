# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def descent(p, original_x = 50, steplength = 0.01):
    ''' gradient descent, return min y '''

    deriv = p.deriv(m = 1) # 多项式p的导函数
    Y = [] # 保存每次迭代后的y值，方便绘图
    count = 0 # 迭代次数
    x = original_x # 设置x初始值
    d = deriv(x) # x位置的导数
    threshold = 0.001 # 阈值，当梯度小于此值时停止迭代

    while np.abs(d) > threshold:
        x = x - d * steplength
        y = p(x)

        Y.append(y)
        count += 1
        d = deriv(x)

    plt.plot(np.arange(1, count + 1), Y)
    plt.show()
    return y

if __name__ == "__main__":
    p = np.poly1d([2, -4, 1])
    min_y = descent(p)
    print(min_y)



