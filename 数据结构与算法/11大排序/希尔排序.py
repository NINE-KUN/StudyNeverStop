items = [5, 6, 8, 9, 10, 3, 2, 4, 1, 7]


def shell_sort(items):
    """希尔排序是对插入排序的优化，基本思路是先选定一个整数作为增量，把待排序文件中的所有数据分组，以每个距离的等差数列为一组，对每一组进行排序，然后将增量缩小，继续分组排序，重复上述动作，直到增量缩小为1时，排序完正好有序。

​     希尔排序原理是每一对分组进行排序后，整个数据就会更接近有序，当增量缩小为1时，就是插入排序，但是现在的数组非常接近有序，移动的数据很少，所以效率非常高，所以希尔排序又叫缩小增量排序。

​     每次排序让数组接近有序的过程叫做预排序，最后一次插入是直接插入排序"""
    gap = int(len(items) / 2)  # 增量最后要减少到1
    while gap > 0:
        for i in range(gap, len(items)):  # 从增量处开始循环
            pos = i - gap    #  获取增量之前的数据索引 从第一个元素开始
            while pos >= 0 and items[pos] > items[pos + gap]:
                items[pos + gap], items[pos] = items[pos], items[pos + gap]
                pos -= gap
        gap = int(gap / 2)
    return items


if __name__ == '__main__':
    print(shell_sort(items))
