"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""

def soulation(nums,target):
    # size = len(nums)
    # res = size +1
    # left, area = 0,0
    # for right,x in enumerate(nums):
    #     area += x  # 右指针一次右移 面积累加
    #     while target <= area: # 判断如果面积符合条件 获取res的值
    #         res = min(res,right-left+1)
    #         area = nums[left]
    #         left += 1
    # return res if res<=size else 0
    if nums is None or len(nums) == 0:
        return 0
    size = len(nums)
    res = size + 1
    left, right, area = 0, 0, 0
    while right < size:
        area += nums[right]
        right += 1
        while area >= target:
            res = min(res, right - left)
            area = area - nums[left]
            left += 1
    if res == size + 1:
        return 0
    else:
        return res

nums = [2,3,1,2,4,3]
target = 7
soulation(nums,target)


