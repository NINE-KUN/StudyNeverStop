# 题目描述
# 输入单行英文句子，里面包含英文字母，空格以及，.﹖三种标点符号，请将句子内每个单词进行倒序，并输出倒序后的语句。
# 输入描述
# 输入字符串s，s的长度1 <= N <= 100
# 输出描述
# 输出逆序后的字符串备注
# 标点符号左右的空格>= 0，单词间空格>0
#
# 示例
# 输入：
# yM eman si boB.
# 输出：
# My name is Bob.
#
# 示例
# 输入：
# woh era uoy ? I ma enif.
# 输出：
# how are you ? I am fine.
#
# 题目解析
# 这道题目比较简单，遍历字符串的每个字符，遇到空格及,.? 对之前缓存的子串进行逆序；
# 逆序后并重置w为空字符串，这里处理需要把空格及,.? 追加到输出队列；
# 字符串遍历结束，使用空字符串拼接列表并输出。

while 1:
    try:
        n=input()
        ret=[]
        w = ''
        for i in n:
            if i in' ,.?':
                ret.append(w[::-1])
                w=''
                ret.append(i)
            else:
                w +=i
        print(''.join(ret))

    except Exception as e:
        break