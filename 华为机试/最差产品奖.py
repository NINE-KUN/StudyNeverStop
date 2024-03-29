'''题目描述
A公司准备对他下面的 N 个产品评选最差奖，评选的方式是首先对每个产品进行评分，然后根据评分区间计算相邻几个产品中最差的产品。
评选的标准是依次找到从当前产品开始前 个产品中最差的产品，请给出最差产品的评分序列。
输入描述
第一行，数字 M，表示评分区间的长度，取值范围是 0 < M < 10000；
第二行，产品的评分序列，比如 12,3,8,6,5 产品数量N 范围是 -10000 < N<10000。
输出描述
评分区间内最差产品的评分序列
示例 1
输入：
3
12,3,8,6,5

输出：
3,3,5

说明：
12,3,8 最差的是 3
3,8,6 中最差的是 3
8,6,5 中最差的是 5'''

while 1:
    try:
        m = int(input())
        num_list = list(map(int,input().split(',')))
        ret = []
        for i in range(m):
            ret.append(str(min(num_list[i:i+m])))
        print(','.join(ret))
    except:
        break

