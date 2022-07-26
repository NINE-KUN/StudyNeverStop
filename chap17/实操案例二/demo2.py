'''变量的赋值'''
name1='林黛玉'
name2='薛宝钗'
name3='贾元春'
name4='贾探春'
name5='史湘云'
print('①\t'+name1)
print('②\t'+name2)
print('③\t'+name3)
print('④\t'+name4)
print('⑤\t'+name5)
'''第2种方式：列表'''
lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['①','②','③','④','⑤']
for i in range(5):
    print(lst_sig[i],lst_name[i])
for s,name in zip(lst_sig,lst_name):
    print(s,name)
'''第三种方式：字典'''
d={'①':'林黛玉','②':'薛宝钗','③':'贾元春','④':'贾探春','⑤':'史湘云'}
for key in d:
    print(key,d[key])
