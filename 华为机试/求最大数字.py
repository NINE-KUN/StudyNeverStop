'''题目描述
给定一个由纯数字组成以字符串表示的数值，现要求字符串中的每个数字最多只能出现 2次，超过的需要进行删除，删除某个重复的数字后，其它数字相对位置保持不变。
如 34533，数字 3 重复超过 2 次，需要删除其中一个3，删除第一个 3 后获得最大数值 4533请返回经过删除操作后的最大的数值，以字符串表示。
输入描述
第一行为一个纯数字组成的字符串，长度范围: [1,100000]。
输出描述
输出经过删除操作后的最大的数值

示例 1
输入：
34533
输出：
4533

示例 2
输入：
5445795045
输出：
5479504
'''

while 1:
    try:
        nums = input()

        i = 1
        while i < len(nums):
            if nums.count(nums[i - 1]) > 2:
                if int(nums[i - 1]) < int(nums[i]):
                    nums = nums[:i - 1] + nums[i:]
                    continue
            i += 1

        # 判断最后一个数字
        if nums.count(nums[-1]) > 2:
            nums = nums[:-1]
        print(nums)
    except Exception as e:
        break
