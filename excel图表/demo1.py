from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
from datetime import date
wb=Workbook()
sh=wb.active
rows=[
    ['date','group1','group2','group3'],
    [date(2022,3,10),43,23,55],
    [date(2022,3,12),56,67,87],
    [date(2022,3,14),34,56,98],
    [date(2022,3,15),83,78,76],
    [date(2022,3,16),15,98,35],
    [date(2022,3,17),34,65,45],
]
for row in rows:
    sh.append(row)

#生成线图表
lc=LineChart()
lc.style=10
lc.title='Line Chart'
lc.x_axis.title='test_number'
lc.y_axis.title='size'
#min_col代表从第几行进行分类
#min_row从第几行开始
#max_col#取到第几列
#max_row取到第几行
data=Reference(sh,min_col=2,min_row=1,max_col=4,max_row=7)
lc.add_data(data,titles_from_data=True)

#将图标增加到sheet
sh.add_chart(lc,'A9')#从第九行开始增加
wb.save('D:\\MoneyLoveLive\\excel图表\\text1.xlsx')