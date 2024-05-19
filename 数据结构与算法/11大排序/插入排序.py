items = [5, 6, 8, 9, 10, 3, 2, 4, 1, 7]


def insert_sort(items):
"""直接插入排序"""
    item = items.copy()
    for i in range(0, len(items)):
        if i != 0:
            for j in range(i):
                if item[j] > item[i]:
                    item[j], item[i] = item[i], item[j]
    return item

def binary_insert_sort(items):
"""折半插入排序"""
    item = items.copy()
    for i in range(0, len(items)):
        temp = item[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = int((low + high) / 2)
            if temp < item[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i - 1, high, -1):  # 因为临时变量保存了第i个值，因此将前面直到high的值依次向后移动，覆盖也没关系
            item[j + 1] = item[j]
        item[high + 1] = temp
    return item


if __name__ == '__main__':
    print(insert_sort(items))
    print(binary_insert_sort(items))
