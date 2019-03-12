#-*- coding: utf-8 -*-
import numpy as np
import operator

'''
    trainData - 训练集
    testData - 测试集
    labels - 分类
'''


def knn(trainData, testData, labels, k):
    # 计算训练样本的行数
    rowSize = trainData.shape[0]
    # 计算训练样本和测试样本的差值
    diff = np.tile(testData, (rowSize, 1)) - trainData
    # 计算差值的平方和
    sqrDiff = diff ** 2
    sqrDiffSum = sqrDiff.sum(axis=1)
    # 计算距离
    distances = sqrDiffSum ** 0.5
    # 对所得的距离从低到高进行排序
    sortDistance = distances.argsort()

    count = {}

    for i in range(k):
        vote = labels[sortDistance[i]]
        count[vote] = count.get(vote, 0) + 1
    # 对类别出现的频数从高到低进行排序
    sortCount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

    # 返回出现频数最高的类别
    return sortCount[0][0]


trainData = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
labels = ['爱情片', '爱情片', '爱情片', '动作片', '动作片', '动作片']
testData = [18, 90]
X = knn(trainData, testData, labels, 3)
print(X)