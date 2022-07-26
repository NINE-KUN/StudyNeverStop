print('-------------创建新excel文件并添加数据---------------------')
def new():
    from openpyxl import Workbook
    wb=Workbook()#创建excel文件
    sh1=wb.active#创建默认表
    sh2=wb.create_sheet('番剧信息')#手动创建表
    wb.save('D:\\MoneyLoveLive\\excel创建和读取\\test2.xlsx')
    '''在表中添加数据'''
    sh2['A1']='咒术回战'
    sh2['A2']='鬼灭之刃'
    wb.save('D:\\MoneyLoveLive\\excel创建和读取\\test2.xlsx')
    '''一次性写入多个数据'''
    rows=[['咒术回战','五条悟'],
          ['鬼灭之刃','碳之郎']]
    for item in rows:
        sh1.append(item)
    wb.save('D:\\MoneyLoveLive\\excel创建和读取\\test2.xlsx')
new()
