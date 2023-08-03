"""冒泡排序"""
"""冒泡排序就是比较相邻的两个数字，如果前者比后者大，就交换位置
    第一位和第二位比较，第一位大，则和第二位交换位置，
    然后第二位和第三位比较，第二位大，则第二位和第三位交换位置"""


def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)


lst = [3, 1, 4, 2]
BubbleSort(lst)
