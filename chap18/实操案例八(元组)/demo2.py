#显示中超联赛前5排名
scores=(('广州恒大',72),('北京国安',70),('上海上港',66),('江苏苏宁',53),('山东鲁能',51))
for index,item in enumerate(scores):
    print(index+1,'.',end='   ')
    for scores in item:
        print(scores,end='   ')
    print()#换行