# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  0:26

# 赋值运算符

# 执行顺序 右→左
a = 20  # 将20赋值给a

# 支持链式赋值
a = b = c = 20
print(a, id(a), b, id(b), c, id(c))

# 支持参数赋值
Num1 = 5

Num1 += 3
print(Num1)  # Num1=Num1+3 Num1=5+3=8

Num1 -= 2
print(Num1)  # Num1=Num1-2 Num1=8-2=6

Num1 *= 2
print(Num1)  # Num1=Num1*2 Num1=6*2=12

Num1 /= 5
print(Num1)  # Num1=Num1/5 Num1=12/5=2.4

Num1 //= 2
print(Num1)  # Num1=Num1//2 Num1=2.4//2=1

Num2 = 7
Num2 %= 2
print(Num2)  # Num2=Num2%2 Num2=7%2=1

Num3 = 2
Num3 **= 3
print(Num3)  # Num3=Num3的3次方 Num3=2*2*2

# 支持系列解包赋值
A, B, C = 10, 20, 30
print(A, B, C)  # 左右两边个数需要一致

# 解包赋值便于变量交换
A, B, C=C, B, A
print(A, B, C)





