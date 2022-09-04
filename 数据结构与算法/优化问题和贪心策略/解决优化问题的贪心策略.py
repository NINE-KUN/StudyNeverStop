'''典型案例
    兑换最少数的硬币:每次照给顾客最少数量的硬币'''

'''找零问题 贪心策略：
    从最大硬币开始 用尽量多的数量优越的 再到下一最大面值的硬币 还用尽量多的数量 一直到结束
    每次都试图解决问题尽量大的一部分(以找零为例 以最多的最大面值来迅速找零)'''

'''找零兑换问题'''

# def changeMoney(n):
#     money = [25, 23, 5, 10, 1]
#     moneylst = sorted(money, reverse=True)
#     j = 0
#     for res in moneylst:
#         j += n // res
#         n = n - n // res * res
#     print(j)


'''找零兑换问题的递归方法'''
'''分析：
    1.先判断是找零是否等于某一个硬币的币值
    2.减小问题规模：
        对每种硬币都尝试一次 如美元硬币体系：
        找零减去1分钱后 求兑换硬币最少数量(递归调用自身)
        找零减去5分后 求兑换硬币最少数量
        找零减去10分后 求兑换硬币最少数量
        找零减去25分后 求兑换一笔最少数量
        上述4项中选择最小的一个'''

'''非常低效 耗时长 大约1min
    377次递归调用 重复调用太多'''
# def recMC(coinValueList, change):
#     minCoins = change
#     if change in coinValueList: #最小规模直接返回 找零等于某个硬币面值
#         return 1
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins = 1 + recMC(coinValueList, change - i)#调用自身
#             if numCoins < minCoins:
#                 minCoins = numCoins
#     return minCoins
#
# print(recMC([1, 5, 10, 25], 63))


'''递归改进 消除重复计算 用表将计算过的中间结果保存起来 在计算之前查看是否已经计算
    这个算法的中间结果就是部分找零的最优解 在递归调用过程中已经得到的最优解被记录下来
    在递归调用之前 先查找表中是否已有部分找零的最优解
    如果有 直接返回最优解而不进行递归调用 如果没有才进行 仅用221次递归调用 0.1毫秒返回'''


def recMC(coinValueList, change, knownReslts):
    minCoins = change
    if change in coinValueList:  # 最小规模直接返回 找零等于某个硬币面值
        knownReslts[change] = 1  # 记录最优解
        return 1
    elif knownReslts[change] > 0:
        return knownReslts[change]  # 查表成功，直接调用最优解
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, \
                                 knownReslts)  # 调用自身
            if numCoins < minCoins:
                minCoins = numCoins
                knownReslts[change] = minCoins #找到最优解，记录到表中
    return minCoins


print(recMC([1, 5, 10, 25], 63, [0] * 64))
