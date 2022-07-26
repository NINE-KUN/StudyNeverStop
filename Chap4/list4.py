# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  14:50
# for-in循环

'''
 1.in表达从（字符串、序列等）中依次取值，又称为遍历
 2.for-in遍历的对象必须是可迭代对象

for-in的语法结构
 for 自定义的变量 in可迭代对象：
     循环体

循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
'''
for item in 'python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5):
    print('要努力学习哦')

print('使用for循环，计算1-100之间的偶数')
sum = 0
for item in range(1,101):
    if item %2 == 0:
        sum += item
print('1-100之间的偶数和为：',sum)

#计算100-999的水仙花数是那几个
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print(item)