# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  23:28

# 比较运算符 比较运算符的返回类型是bool类型
a = 10
b = 20
print(a > b)  # False 比较二者的值 Value
print(a < b)  # True 比较二者的值 Value
print(a <= b)  # True 比较二者的值 Value
print(a >= b)  # False 比较二者的值 Value
print(a == b)  # False 比较二者的值 Value
print(a != b)  # True 比较二者的值 Value

a = 30
b = 30
print(id(a), id(b))
print(a is b)  # True 比较二者的标识符 Id 该表达式意为 a的id和b的id相同
print(a is not b)  # False 比较二者的标识符 Id 该表达式意为 a的id和b的id不相同

list1 = [10, 20, 30, 40]
list2 = [10, 20, 30, 40]
print(id(list1), id(list2))
print(list1 is list2)  # False 比较两个集合的id(标识符)

# 布尔运算符 对于布尔值之间的运算

print('---------- and 与 二元布尔运算符----------')
print('全部为真Ture 则返回值为真Ture， 一个为假False则返回值为假False')
a = 10
b = 20
print(a == 10 and b == 20)  # True and Ture -->Ture
print(a != 10 and b == 20)  # False and Ture --> False
print(a != 10 and b != 20)  # False and False --> False

print('----------or 或 二元布尔运算符----------')
print('有一个为真Ture则返回值为真Ture，两个为假False则返回值为假False')
a = 20
b = 30
print(a == 20 or b == 30)  # Ture or Ture --> Ture
print(a != 20 or b == 30)  # False or Ture --> Ture
print(a != 20 or b != 30)  # False or False --> False

print('----------not 不是 一元布尔运算符 对布尔类型操作数取反----------')
T = True
F = False
print(not T)  # True -->False T 不是该值(该值为True) 取反则为False
print(not F)  # False -->True F 不是该值(该值为False) 取反则为True

print('----------in 和 not in 在里面和不在里面---------- ')
H = 'HelloWord'
print('o' in H)  # 字母o在HelloWorld里面 结果为True
print('k' not in H)  # 字母k不在HelloWorld里面 结果为True
print('e' not in H)  # 字母e不在HelloWorld里面 结果为Flase



