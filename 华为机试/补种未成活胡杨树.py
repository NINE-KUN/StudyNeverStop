'''
题目 补种未成活胡杨树
某沙漠新种植 N 颗胡杨（编号 1~N），
一个月后，有 M 颗未能成活。
现可补种 K 颗（只可补种，不可新种）
，请问怎样补种，可以得到最多的连续胡杨树？

输入描述
N 总种植数量
M 未成活数量
M 个空格分割的数，按编号从小到大排列
K 最多可以补种的数量
其中 1<=N<1000 1<=M<N 0<=K<=M

输出描述：
可以得到最多的连续胡杨树？

示例
输入
10
3
2 4 7
1
输出
6
'''

while 1:
    try:
        n = int(input())
        m = int(input())
        nums = list(map(int, input().split()))
        k = int(input())

# 首先生成树苗状态的二位数组
        nums = [0 if i + 1 in nums else 1 for i in range(n)]
        max_ = 0
# 滑动窗口边界
        i = 0
        j = min(k, n)
        while j <= len(nums):
            # 求子串中0的个数
            count = nums[i:j].count(0)
            if count < k:
                j += 1
            elif count == k:
                max_ = max([j-i, max_])
                j += 1
            else:
                i += 1

        print(max_)
    except Exception as e:
        break
