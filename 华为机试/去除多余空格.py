'''去除多余空格
题目
去除文本多余空格，但不去除配对单引号之间的多余空格。给出关键词的起始和结束下标，去除多余空格后刷新关键词的起始和结束下标。
条件约束：
不考虑关键词起始和结束位置为空格的场景；
单词的的开始和结束下标保证涵盖一个完整的单词，即一个坐标对开始和结束下标之间不会有多余的空格；
如果有单引号，则用例保证单引号成对出现；
关键词可能会重复；
文本字符长度length取值范围：[0, 100000];'''

'''输入
输入为两行字符串：
第一行：待去除多余空格的文本，用例保证如果有单引号，则单引号成对出现，且单引号可能有多对。
第二行：关键词的开始和结束坐标，关键词间以逗号区分，关键词内的开始和结束位置以单空格区分。
例如：
Life is painting a  picture, not doing 'a  sum'.
8 15,20 26,43 45

关键单词为：painting picture sum
输出
输出为两行字符串：
第一行：去除多余空格后的文本
第二行：去除多余空格后的关键词的坐标开始和结束位置，为数组方式输出。
例如：
Life is painting a picture, not doing 'a  sum'.
[8, 15][19, 25][42, 44]'''


st=input()
pre_keyword=input().split(',')
key_word=[list(map(int,pre_keyword[i].split())) for i in range(len(pre_keyword))]
stack=[]
space=[]
pre_value=' '
for i,value in enumerate(st):
    if not stack:
        if value=="'":
            stack.append("'")
        elif pre_value==' ' and value==' ':
                space.append(i-1)
    elif value=="'":
            stack.pop()
    pre_value=value
for i in range(len(key_word)):
    for j in range(2):
        count=0
        for k in space:
            if key_word[i][j]>=k:
                count+=1
        key_word[i][j]-=count
lst=list(st)
for item in space:
    lst.pop(item)
print(''.join(lst))
print(key_word)









