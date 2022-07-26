# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:09
'''b 以二进制方式打开文件 不能单独使用 需要与其他模式一起使用 rb或wb'''
'读取已有文件'
src_file=open('b.txt','rb')
'写入'
target_file=open('copyb.txt','wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()
