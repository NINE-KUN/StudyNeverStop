
print('---------------向文件输出内容--------------------------')
'''第一种方式：使用print方式进行输出(输出的目的地是文件)'''
fp=open('D:/MoneyLoveLive/chap17/test.txt','w')
print('自律即自由',file=fp)
fp.close()

'''第二种方式：使用文件读写操作'''
with open('D:/MoneyLoveLive/chap17/test1.txt','w') as file:
    file.write('自律即自由')

print('--------------输出天气预报---------------------------')
print('星期四','今天')
print('---------------------------------------------------')
print('08时','11时','14时','17时','20时','23时')
print('0℃ ','6℃ ','11℃','12℃','13℃','14℃',)
print('---------------------------------------------------')
print('明  天','2/24','2℃/11℃')
print('星期五','2/25','0℃/9℃')
print('星期六','2/26','-2℃/-3℃')
print('星期天','2/27','-3℃/0℃')
print('星期一','2/28','2℃/11℃')

print('-------------------机票购买界面-----------------------')
print('✈国内\t','✪国际、港澳台\t','↘发现低价')
print('------------------------------------------')
print('航班类型\t','⊙单程\t','⊙往返\t','⊙多程(含缺口程)')
print('出发城市:青海')
print('到达城市：成都')
print('出发日期：2022/2/24')
print('返回日期：yyyy-MM-dd')
print('------------------------------------------')
print('\t\t◻带儿童','\t◻带婴儿')
print('\t\t\t_______')
print('\t\t\t|_搜索_|')