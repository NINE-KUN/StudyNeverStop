# k近邻法(k-nearest neighbor, k-NN)是1967年由Cover T和Hart P提出的一种基本分类与回归方法。
# 它的工作原理是：存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一个数据与所属分类的对应关系。
# 输入没有标签的新数据后，将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。
# 一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。
# 最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。
#
# 举个简单的例子，我们可以使用k-近邻算法分类一个电影是爱情片还是动作片。
#
# 电影名称	打斗镜头	接吻镜头	电影类型
# 电影1	1	     101	爱情片
# 电影2	5	      89	爱情片
# 电影3	108	       5	动作片
# 电影4	115        8	动作片
# 每部电影的打斗镜头数、接吻镜头数以及电影类型
# 我们已有的数据集合，也就是训练样本集。
# 这个数据集有两个特征，即打斗镜头数和接吻镜头数。
# 除此之外，我们也知道每个电影的所属类型，即分类标签。
# 用肉眼粗略地观察，接吻镜头多的，是爱情片。打斗镜头多的，是动作片。
# 以我们多年的看片经验，这个分类还算合理。
# 如果现在给我一部电影，你告诉我这个电影打斗镜头数和接吻镜头数。
# 不告诉我这个电影类型，我可以根据你给我的信息进行判断，这个电影是属于爱情片还是动作片。
# 而k-近邻算法也可以像我们人一样做到这一点，而k-邻近算法是靠已有的数据。
# 比如，你告诉我这个电影打斗镜头数为2，接吻镜头数为102，我的经验会告诉你这个是爱情片，k-近邻算法也会告诉你这个是爱情片。

# 比如该电影散点位置在(101,20) 已知（1，101）和（5，89）为爱情片 ， (108,5)和(115,8)为动作片
# 我们可以从散点图大致推断，这个红色圆点标记(101,20)的电影可能属于动作片，因为距离已知的那两个动作片的圆点更近。
# k - 近邻算法用什么方法进行判断呢？没错，就是距离度量。
# 这个电影分类的例子有2个特征，也就是在2维实数向量空间，可以使用我们高中学过的两点距离公式计算距离。


#  通过计算，我们可以得到如下结果：
#
# (101,20)->动作片(108,5)的距离约为16.55
# (101,20)->动作片(115,8)的距离约为18.44
# (101,20)->爱情片(5,89)的距离约为118.22
# (101,20)->爱情片(1,101)的距离约为128.69


# 通过计算可知，红色圆点标记的电影(101,20)到动作片 (108,5)的距离最近，为16.55。
# 如果算法直接根据这个结果，判断该红色圆点标记的电影为动作片，
# 这个算法就是最近邻算法，而非k-近邻算法。那么k-邻近算法是什么呢？k-近邻算法步骤如下：
#
"""计算已知类别数据集中的点与当前点之间的距离；
按照距离递增次序排序；
选取与当前点距离最小的k个点；
确定前k个点所在类别的出现频率；
返回前k个点所出现频率最高的类别作为当前点的预测分类。
比如，现在我这个k值取3，
那么在电影例子中，按距离依次排序的三个点分别是动作片(108,5)、动作片(115,8)、爱情片(5,89)。
在这三个点中，动作片出现的频率为三分之二，爱情片出现的频率为三分之一，所以该红色圆点标记的电影为动作片。
这个判别过程就是k-近邻算法。"""

# 1.3.1 准备数据集
import numpy as np

# 函数说明:创建数据集
#
# Parameters:
#     无
# Returns:
#     group - 数据集
#     labels - 分类标签
# Modify:

# -*- coding: UTF-8 -*-
import numpy as np
import operator

"""
函数说明:创建数据集

Parameters:
    无
Returns:
    group - 数据集
    labels - 分类标签
Modify:
    2017-07-13
"""


def createDataSet():
    # 四组二维特征
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    # 四组特征的标签
    labels = ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels


"""
函数说明:kNN算法,分类器

Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果

Modify:
    2017-07-13
"""


def classify0(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    # np.tile(inX, (dataSetSize, 1))创建红点标记(101,20)的dateset 四行两列
    # 0          1
    # 101        20
    # 101        20
    # 101        20
    # 101        20
    # 然后通过红色标记点-数据集标记点
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    # sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方，计算出距离
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]


if __name__ == '__main__':
    # 创建数据集
    group, labels = createDataSet()
    # 测试集
    test = [101, 20]
    # kNN分类
    test_class = classify0(test, group, labels, 3)
    # 打印分类结果
    print(test_class)
