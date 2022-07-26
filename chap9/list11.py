# 用 户 ： 钱坤
# 使 用 人：钱坤
# 目 的：学习 赚钱
# 开发时间：  12:30
lst=[{'rating':[9.7,50],'id':'1292052','type':['犯罪','剧情'],'title':'肖生客的救赎','actors':['蒂姆罗宾斯','摩根弗里曼']},
     {'rating':[9.6,5],'id':'1292026','type':['爱情','剧情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅']},
     {'rating':[9.6,50],'id':'1292066','type':['犯罪','剧情','悬疑'],'title':'控方证人','actors':['泰隆鲍华','玛琳黛德丽']},
     ]
''' 要求输入演员名字输出参演的电影名称'''
name=input('请输入演员姓名')
for item in lst:
    lst_actor = item['actors']
    for actor in lst_actor:
        print(actor)
        if name in actor:
           print(name,'参演了',item['title'])

