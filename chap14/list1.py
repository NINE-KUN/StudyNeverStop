# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  11:31
file=open('a.txt','r',encoding='utf-8')
print(file.readline())
file.close()

'''w 写入操作 会将原有文件内容进行覆盖'''
file=open('a.txt','w',encoding='utf-8')
file.write('Python')
file.close()

'''a 以追加模式打开文件 如果文件不存在则创建 文件指针在文件开头 如果文件存在 则在文件末尾追加内容 文件指针在源文件末尾'''
file=open('a.txt','a',encoding='utf-8')
file.write('Python')
file.close()
