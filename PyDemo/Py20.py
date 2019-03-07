#-*- coding: utf-8 -*-
from numpy import *
import operator
def classify(inputPoint,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]     #已知分类的数据集（训练集）的行数
    #先tile函数将输入点拓展成与训练集相同维数的矩阵，再计算欧氏距离
    diffMat = tile(inputPoint,(dataSetSize,1))-dataSet  #样本与训练集的差值矩阵
    sqDiffMat = diffMat ** 2                    #差值矩阵平方
    sqDistances = sqDiffMat.sum(axis=1)         #计算每一行上元素的和
    distances = sqDistances ** 0.5              #开方得到欧拉距离矩阵
    sortedDistIndicies = distances.argsort()    #按distances中元素进行升序排序后得到的对应下标的列表
    #选择距离最小的k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[ sortedDistIndicies[i] ]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    #按classCount字典的第2个元素（即类别出现的次数）从大到小排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]


if __name__ == "__main__" :
    dataset = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    X = array([1.2, 1.1])
    Y = array([0.1, 0.1])
    k = 3
    labelX =classify(X,dataset,labels,k)
    labelY =classify(Y,dataset,labels,k)
    print("Your input is:", X, "and classified to class: ", labelX)
    print("Your input is:", Y, "and classified to class: ", labelY)

