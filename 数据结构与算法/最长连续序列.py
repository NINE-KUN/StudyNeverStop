"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_len = 0
        for num in nums:
            if num-1 not in nums:  # 判断是否为开头的数
                current_num = num  # 将此数赋值给current_num 用于查找后续连续的数
                current_streak = 1  # 记录1次
                while current_num+1 in nums:  # 当current_num 这个开头的数+1 后面一位数在该列表
                    current_num += 1  # 该数继续+1 判断后面一位是否存在
                    current_streak += 1  # 记录加1
                longest_len = max(longest_len,current_streak)
        return longest_len

  if __name__ == '__main__':
    s=Solution()
    s.longestConsecutive([100,4,200,1,3,2])






"""
解题思路：
怎么判断呢，就是用哈希表查找这个数前面一个数是否存在，即num-1在序列中是否存在。存在那这个数肯定不是开头，直接跳过。
因此只需要对每个开头的数进行循环，直到这个序列不再连续，因此复杂度是O(n)。 以题解中的序列举例:
[100，4，200，1，3，4，2]
去重后的哈希序列为：
[100，4，200，1，3，2]
按照上面逻辑进行判断：
元素100是开头,因为没有99，且以100开头的序列长度为1
元素4不是开头，因为有3存在，过，
元素200是开头，因为没有199，且以200开头的序列长度为1
元素1是开头，因为没有0，且以1开头的序列长度为4，因为依次累加，2，3，4都存在。
元素3不是开头，因为2存在，过，
元素2不是开头，因为1存在，过。
"""
