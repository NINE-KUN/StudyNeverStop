# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  15:57
#获取列表中的多个元素
'''
  列表名[start:stop:step]
  切片的结果：原列表片段的拷贝(属于一个新列表)
  切片范围：[start:stop) 从start开始 到stop 不包括stop
  step：默认步长为1 简写为[stop:step]
'''

lst=[10,20,30,40,50,60,70,80,90]
print(lst)
print(lst[1:7]) # step什么都不写，默认步长为1
lst2=lst[1:7]
print('原列表id',id(lst))
print('原列表切片id：',id(lst2))
print(lst[1:6:]) #省略步长 默认步长为1
print(lst[1::2]) #省略stop 默认stop为全部
print(lst[:6:2]) #省略start 默认start为0

# step 为负数 切片的第一个元素为默认列表的最后一个元素 (逆输出)
print('----------step(步长)为负数----------')
print('原列表',lst)
print(lst[::-1])
print(lst[:5:-2])
print(lst[8::-2])

