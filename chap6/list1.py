# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  16:47

# 字典
'''
 python内置的数据结构之以，与列表一样是一个可变序列
 以键值对的方式存储，字典是一个无序的序列
 python中的字典是根据key值查找value的(通过计算hash函数查找出key值所对应的Value)
'''

# 创建字典
scores={'钱坤':26,'邹涛':25,'魏万卉':25}
print(scores,type(scores))
# 使用内置函数创建字典
stu=dict(name='QianKun',age=26)
print(stu,type(stu))

# 创建空字典
nulld={}

# 获取字典中的元素
'''
   第一种方式，使用[]
   如果查询key值不存在 将抛出异常 KeyError
'''
print(scores['邹涛'])
'''
   第二种方式，使用get()方法
   该方法如查询key不存在 返回None 不存在时可提供默认值
'''
print(scores.get('邹涛'))
print(scores.get('阿涛')) # 键值不存在 返回None
print(scores.get('涛尼玛',25))

# 字典的判断
print('阿涛' in scores) #键值存在在字典 返回Ture
print('阿涛' not in scores) #键值不存在于字典 返回False

#字典的删除
del scores['魏万卉']
'''scores.clear() # 清空字典'''
print(scores)

# 新增字典中的元素
scores['魏万卉']=25
print(scores)

# 修改字典中的元素
scores['邹涛']=26
print(scores)