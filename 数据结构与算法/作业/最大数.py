# 给定一组非负整数nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
# 示例1：
# 输入：nums = [10, 2]
# 输出："210"
#
# 示例2：
# 输入：nums = [3, 30, 34, 5, 9]
# 输出："9534330"
import functools


class Solution:
    # 若拼接字符串 x+y>y+xx + y > y + xx+y>y+x ，则 xxx “大于” yyy 。
    # 反之，若 x+y<y+xx + y < y + xx+y<y+x ，则 xxx “小于” yyy 。
    # 先把nums中的所有数字转化为字符串，形成字符串数组 nums_str
    # 比较两个字符串x,y的拼接结果x+y和y+x哪个更大，从而确定x和y谁排在前面；将nums_str降序排序
    # 把整个数组排序的结果拼接成一个字符串，并且返回
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(key=functools.cmp_to_key(compare))
        res = ''.join(nums_str)
        if res[0] == '0':
            res = '0'
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
