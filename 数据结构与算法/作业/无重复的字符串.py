# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。

def lenStr(s):
    """方法一"""
    lst = []
    for i in s:
        lst.append(i)
    lst = set(lst)
    return len(lst)

    # 方法二
    # lst=[]
    # for i in range(len(s)):
    #     if s[i] not in lst:
    #         lst.append(s[i])
    # return len(lst)



if __name__ == '__main__':
    print(lenStr("abcabcbb"))
