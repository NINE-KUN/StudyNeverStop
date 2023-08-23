"""首先选择一个基准数，然后遍历数组，
    比基准数小的放在基准数左边，把基准数大的放在基准数的右边
    左边的数和右边的数进行递归 O（nlogn）"""


def QuickSortPivot(a, start, end):
    pivot = start
    # j代表大于基准数的数的下表左边界
    j = start + 1
    # 遍历当前列表的所有数
    for i in range(start + 1, end + 1):
        # 如果当前数小于等于基准数 则当前数a[i]和a[j]交换
        # j自增
        # 这段话目的保证j下标的数都是小于等于基准数
        if a[i] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    # 把基准数a[pivot]和a[j-1]进行交换
    # 也就是将基准数和小于基准数的的最后一位交换，这样基准数前面都小于基准数，后面都大于基准数
    a[pivot], a[j - 1] = a[j - 1], a[pivot]
    # 然后更新基准数的下标
    pivot = j - 1
    print(a[pivot], a[start:pivot], a[pivot + 1:end + 1])
    # 返回基准数下表
    return pivot


def QuickSort(a, start, end):
    """递归执行快速排序"""
    if start >= end:
        # 如果只有一个数字直接返回
        return
    # 否则利用之前实现的函数，获取区间内的基准下标，分别递归计算
    pivot = QuickSortPivot(a, start, end)
    # 递归基准数左边部分
    QuickSort(a, start, pivot - 1)
    # 递归基准数右边部分
    QuickSort(a, pivot + 1, end)


a = [8,5,12,6,4,3,7,9,2,1,10,11]
QuickSort(a, 0, 11)
print(a)
