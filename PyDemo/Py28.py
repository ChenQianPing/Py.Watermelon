# coding=utf-8
from numpy import *
import time

def loadSimpData():
    datMat = matrix([[1.0, 2.1],
                     [2., 1.1],
                     [1.3, 1.],
                     [1., 1.],
                     [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = [];
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def stumpClassify(dataMatrix, dimen, threshVal, threshIneg):
    # 初始化数据类别都为+1
    # 分左右子树
    # 与阀值比较，左子树小于阀值为-1，大于阀值为1。右侧大于阀值为-1，小于阀值为1。
    # 这两种分法，最后取错误率最低的分法
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneg == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray


def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr);
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0;
    bestStump = {};
    bestClasEst = mat(zeros((m, 1)))
    minError = inf
    # 循环取样本的第i个特征
    for i in range(n):
        # 求出每一列的最大最小值
        rangeMin = dataMatrix[:, i].min();
        rangeMax = dataMatrix[:, i].max();
        # 步长
        stepSize = (rangeMax - rangeMin) / numSteps
        # 这一个循环用来调整阀值
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                # 计算阀值
                threshVal = (rangeMin + float(j) * stepSize)
                # 计算预测标签
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                # 错误矩阵，用来记录预测错误的样本
                errArr = mat(ones((m, 1)))
                # 实际标签与预测标签相等的为0
                errArr[predictedVals == labelMat] = 0
                # 权重向量D乘错误矩阵，预测正确的权重为零，权重就无需更改
                weightedError = D.T * errArr
                # 与最小错误比较
                # print ("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))
                if weightedError < minError:
                    # 更新最小错误
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal

    print("bestsplit: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (
    bestStump['dim'], bestStump['thresh'], bestStump['ineq'], minError))
    # 返回的是bestStump中保存的单层决策树（就是选择出了两类中能使错误率降到最低的特征）
    # 最小错误率，最好的类别预测
    return bestStump, minError, bestClasEst


def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []
    m = shape(dataArr)[0]
    # D是一个概率分布向量，其和要等于1，因此要除以m
    # 权重的初始化可以是一样的随着迭代次数增加
    # 增加错误分类的权重，降低错误分类的权重
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        # 创建一个弱学习器（树根）
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        print("D:", D.T)
        # Adaboost为每一个弱分类器都分配一个权重alpha
        # 这些alpha值都是基于每一个弱分类器的错误率进行计算
        # 计算公式alpha = 1/2ln(1-c/c)
        # c是错误率c=错误分类的样本个数/所有样本总数
        # 为了防止分母为零，增加1e-16
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        # 存到树根中
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print("classEst: ", classEst.T)
        # 更新权重向量D
        # 正确分类的expon为负（权重影响小）
        # 错误分类的expon为正（权重影响大）
        # 这里正确标签和预测样本标签相乘，标签一样为正，不一样为负
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()

        aggClassEst += alpha * classEst
        # sign if a>0 return 1,if a<0 return -1,if a==0 return 0
        # 计算错误分类的个数
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        # 错误率
        errorRate = aggErrors.sum() / m
        print("total error: ", errorRate)
        if errorRate == 0.0: break
    # 返回每一次迭代获得的最好结果的分类器
    # 弱分类器参数集合，和每一个弱分类器对应的alpha（权重）
    return weakClassArr, aggClassEst


def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    # classifierArr是最优分类器的集合
    for i in range(len(classifierArr)):
        # 调用训练好的分类器参数
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], \
                                 classifierArr[i]['thresh'], \
                                 classifierArr[i]['ineq'])
        # 这些分类器使用投票的方式，获得最终的预测结果
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print(aggClassEst)
    return sign(aggClassEst)


# ROC曲线的绘制及AUC计算函数
def plotROC(predStrengths, classLabels):
    import matplotlib.pyplot as plt
    cur = (1.0, 1.0)
    # AUC的值
    ySum = 0.0
    # 计算分类为正的个数
    numPosClas = sum(array(classLabels) == 1.0)
    yStep = 1 / float(numPosClas);
    xStep = 1 / float(len(classLabels) - numPosClas)
    # predStrengths是投票预测结果（非整数），argsort()从大到小排序，返回下标
    # 也就是预测结果接近于1（分类为正）的排在前面
    sortedIndicies = predStrengths.argsort()
    # print('predStrengths',predStrengths)
    # print('classLabels',classLabels)
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    # classLabels是真实结果，通过比较，为正类，移动y轴，否则移动x轴
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0;
            delY = yStep;
        else:
            delX = xStep;
            delY = 0;
            ySum += cur[1]
        ax.plot([cur[0], cur[0] - delX], [cur[1], cur[1] - delY], c='b')
        cur = (cur[0] - delX, cur[1] - delY)
    ax.plot([0, 1], [0, 1], 'b--')
    plt.xlabel('False positive rate');
    plt.ylabel('True positive rate')
    plt.title('ROC curve for AdaBoost horse colic detection system')
    ax.axis([0, 1, 0, 1])
    plt.show()


def test():
    datMat, classLabels = loadSimpData()
    # D = mat(ones((5,1))/5)
    # buildStump(datMat,classLabels,D)
    # 以上就构成了一个弱分类器
    # 接下来训练出多个弱分类器，构成Adaboost算法
    classifierArray = adaBoostTrainDS(datMat, classLabels, numIt=9)
    print(classifierArray)
    # 接下来进行测试


# 实例对马疝病数据集分类使用Adaboost
def app():
    datArr, labelArr = loadDataSet('horseColicTraining2.txt')
    classifierArray = adaBoostTrainDS(datArr, labelArr, 10)

    testArr, testLabelArr = loadDataSet('horseColicTest2.txt')
    prediction10 = adaClassify(testArr, classifierArray)
    errArr = mat(ones((67, 1)))
    errArr[prediction10 != mat(testLabelArr).T].sum()


# 画ROC曲线图
def plotROCtest():
    datArr, labelArr = loadDataSet('horseColicTraining2.txt')
    classifierArray, aggClassEst = adaBoostTrainDS(datArr, labelArr, 10)
    plotROC(aggClassEst.T, labelArr)


if __name__ == '__main__':
    # start = time.clock()

    test()
    # app()
    # plotROCtest()

    # end = time.clock()
    print('finish all')
    # print('finish all in %s' % str(end - start))
