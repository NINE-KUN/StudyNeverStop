# 给你一个字符串s，找到s中最长的回文子串。如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 示例1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba"同样是符合题意的答案。

def longestPalindrome(s):
    res = ''
    for i in range(len(s)):
        # 定位到回文词开头前一位，因为可能小于0，所以做一个截断
        # len(res)是获取当前找到的最长回文字串，i为左边界，左边界-1-len(res)就可以获取上一次的字串
        right = max(0,i - len(res) - 1)
        temp = s[right:i + 1]
        """最后，根据选定的回文子串的索引范围，对字符串做切片，并判断是否是回文子串。
        这里需要注意，此时分为开头讨论的两种情况，即奇数个回文子串和偶数个回文子串，命中其一种条件，
        就把寻找到的回文子串重新赋值给res，这样res的长度会随着指针的遍历越来越大，遍历结束后，res即为最长回文子串。
        """
        if temp == temp[::-1]:
            res = temp
        else:
            temp = temp[1:]
            if temp == temp[::-1]:
                res = temp
    return res

if __name__ == '__main__':
    print(longestPalindrome('babad'))
