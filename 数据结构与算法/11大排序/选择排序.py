"""选择排序"""
"""选择排序就是将 第一个元素到最后一个元素中，找到最小的元素，将最小的元素和第一个元素进行交换，
    然后从第二个元素到最后一个元素，找到一个最小的元素，将最小的元素和第二个元素进行交换"""

def SelectionSort(lst):
    """第一种方式"""
    # n = len(lst)
    # for i in range(n - 1):
    #     min_position = i
    #     for j in range(i + 1, n):
    #         if lst[j] < lst[min_position]:
    #             min_position = j
    #     lst[i], lst[min_position] = lst[min_position], lst[i]
    #     print(lst)
    """第二种方式"""
    n = len(lst)
    for i in range(n - 1):
        min_num = lst.index(min(lst[i:n]))
        lst[i], lst[min_num] = lst[min_num], lst[i]
        print(lst)


lst = [3, 5, 4, 6, 2, 9, 8, 7, 1]
SelectionSort(lst)

