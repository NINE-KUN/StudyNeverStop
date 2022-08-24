'''python中None只有一个 赋值给变量时 变量的地址便指向None的地址'''
a=None
b=None
print(id(a)==id(b))