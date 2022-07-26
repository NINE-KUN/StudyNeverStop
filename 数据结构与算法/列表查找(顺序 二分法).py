'''顺序查找(线性查找)
   从列表第一个元素开始，顺序进行搜索，直到找到 '''


def linear_search(lst, val):  # 时间复杂度O(n)
    for ind, v in enumerate(lst):
        if v == val:
            return ind
        else:
            return None


'''二分法查找(折半查找) 先进行排序 然后比较需要查找的值与中间值 
   是在中间值的哪个区域 然后再次不叫所选区域的中间值进行比较 选出区域 以此类推'''


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(nums, 3))
