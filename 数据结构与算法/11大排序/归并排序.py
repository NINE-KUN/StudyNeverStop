def merge(left,right):
    """用于将两个有序列表合并成一个有序列表"""
    left_index , right_index =0, 0  # 左子序列索引 ， 右子序列索引
    result = []
    while left_index < len(left) and right_index < len(right):  # 判断索引没有超出序列范围
        if left[left_index] < right[right_index]: # 如果左子序索引小于右子序列索引
            result.append(left[left_index]) # 列表追加左子序列该索引的值
            left_index +=1  # 左子序列索引加一供下一次比较
        else:
            result.appernd(right[right_index]) # 否则列表追加右子序列该索引的值
            right_index +=1 # 右子序列加一供下一次比较
    result += left[left_index:] # 列表先追加左子序列 (较小的序列)
    result += right[right_index:] # 然后列表追加右子序列 (较大的值)
    return reslut

def merge_sort(alist):
    """将一个无序列表排序"""
    if len(alist) <=1: 
        return alist
    num = len(alist) // 2  # 从中间划分为左右两个子序列
    left = merge_sort(alist[:num])  # 对左子序列进行递归排序
    right = merge_sort(alist[num:])  # 对右子序列进行递归排序
    return merge(left,right) # 归并


