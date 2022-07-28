# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:29

# 格式化字符串

# 1. % 占位符 %sstr类型 %d整数类型 %f浮点类型
name='钱坤'
age=25
print('我叫%s,今年%d'%(name,age))

# 2.{}占位符
print('我叫{0},今年{1}，我一直都叫{0}'.format(name,age))

# 3.f-string
print(f'我叫{name},今年{age}')

print('%10d'%99) # 10表示的是宽度
print('%f'%3.1415926)
print('%.3f'%3.1415926) #.3 指表示小数点后3位
print('%10.3f'%3.1415926) # 同时表示了宽度和精度 宽度为10 精度为小数点后3位

print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926)) # .3表示一共是3位数
print('{0:.3f}'.format(3.1415926)) # .3f表示3位小数
print('{0:10.3f}'.format(3.1415926)) # 10宽度为10 .3f表示3位小数 同时设置宽度精度
