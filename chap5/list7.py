# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  14:48

# 元素列表的排序操作
'''
常见的方式有两种
       sort() 不生成新列表
       sorted() 生成新的列表
       参数设置
         reverse=True列表进行降序操作
         不写参数或reverse=False 列表进行升序操作
'''
lst=[22,11,55,77,66,88,99]
print('原列表',lst,id(lst))
# 开始排序
lst.sort()
print('升序排序后列表',lst,id(lst))
#开始降序排序
lst.sort(reverse=True)
print('降序排序后的列表',lst,id(lst))

print('----------使用sorted()内置函数进行排序,将产生一个新的列表对象----------')
lst=[11,55,22,66,88,77]
print('原列表',lst,id(lst))
new_lst=sorted(lst)
print('升序后列表',new_lst,id(new_lst))
desc_lst=sorted(lst,reverse=True)
print('降序后列表',desc_lst,id(desc_lst))
