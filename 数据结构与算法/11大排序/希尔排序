items = [5, 6, 8, 9, 10, 3, 2, 4, 1, 7]


def shell_sort(items):
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
