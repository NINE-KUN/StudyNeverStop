#编写程序输入学员成绩
try:
    score=int(input('请输入你的分数'))
    if 0<score<=100:
        print('分数为:',score)
    else:
        raise Exception('分数不正确')
except Exception as e:#如果没有写try except异常由python捕获 如果有则由except 捕获
    print(e)

print('----------------------------------------------')
score=int(input('请输入你的分数'))
if 0<score<=100:
    print('分数为:',score)
else:
    raise Exception('分数不正确')