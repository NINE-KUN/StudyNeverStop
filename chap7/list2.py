# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  18:20

# 元组为防止多用户数据修改逐个上锁 所以为不可变序列
t=(10,[20,30],40)
'''
  元组中包含 int 和列表 
   列表中的元素可以增删改 
   注意事项
      1.如果元组中的对象本身不可变对象，则不能再引用其他对象
      2.如果元组中的对象是可变对象，则可变对象的引用不允许改变，但可以改变数据
'''
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
print('----------[20,30]为列表，而列表是可变序列，所以可以在列表中添加元素，而列表内存地址不变----------')
t[1].append(100)
print(t,id(t[1]))
t[1].insert(2,8)
print(t,id(t[1]))