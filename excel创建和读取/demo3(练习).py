from openpyxl import Workbook
def new():
    wb=Workbook()
    sh1=wb.active
    sh1.title='video'
    sh2=wb.create_sheet('大佬们')
    rows=[['鬼灭之刃','音柱',80,'日本'],
          ['jojo的奇幻冒险','jojo',90,'日本'],
          ['Dota2龙之血','伊利丹',95,'美国'],
          ['镇魂街','典韦',89,'中国'],
          ['一拳超人','琦玉老师',99,'日本']
          ]
    for row in rows:
        sh1.append(row)
        print(row)
        if row[2]>=90 and row[3]=='日本':
            sh2.append(row)
    wb.save('D:\\MoneyLoveLive\\excel创建和读取\\test3.xlsx')
new()