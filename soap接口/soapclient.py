#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suds.client import Client  # 导入suds.client 模块下的Client类

wsdl_url = "http://localhost:8088/?wsdl"
client = Client(wsdl_url)
print(client)

MsgHeader = client.factory.create('ns3:T_MsgHeader')
print(MsgHeader)
MsgHeader.BATCH_NO = ''
MsgHeader.TOTAL_PAGE = ''
MsgHeader.CURRENT_PAGE = ''
MsgHeader.PAGE_SIZE = ''
MsgHeader.TOTAL_COUNT = ''
MsgHeader.TOKEN = ''
MsgHeader.SUBMIT_DATE = ''
MsgHeader.SELLOUT_TYPE = ''
MsgHeader.PARTNER_TYPE = ''
MsgHeader.LOGISTICS_PLATFORM = ''
MsgHeader.PARTNER_ID = ''
MsgHeader.PARTNER_NAME = ''

MsgLine = client.factory.create('ns3:T_MsgLine')
print(MsgLine)
MsgLine.PARTNER_ID = ''
MsgLine.FINAL_CUST_ID = ''
MsgLine.FINAL_CUST_NAME = ''
MsgLine.HW_ITEM_CODE = ''
MsgLine.QTY = ''
MsgLine.DATE = ''
MsgLine.SHIP_TO_ADDRESS = ''
MsgLine.SHIP_FROM_PROVINCE = ''
MsgLine.SHIP_FROM_CITY = ''
MsgLine.HW_SALES_PERSON = ''
MsgLine.HW_PRODUCTS_PERSON = ''
MsgLine.HW_CHANNEL_PERSON = ''
MsgLine.INDUSTRY = ''
MsgLine.RETURN_REASON = ''
MsgLine.ECOMMERCE_PLATFORM_NAME = ''
MsgLine.ECOMMERCE_STORE_TYPE = ''
MsgLine.PARTNER_ID = ''

MsgLines = client.factory.create('ns3:T_MsgLines')
MsgLines['MsgLine'] = MsgLine
print(MsgLines)

party = client.factory.create('ns2:party')

print(party)


# def say_hello_test(url, name, times):
#     client = Client(url)                    # 创建一个webservice接口对象
#     client.service.say_hello(name, times)   # 调用这个接口下的getMobileCodeInfo方法，并传入参数
#     req = str(client.last_sent())           # 保存请求报文，因为返回的是一个实例，所以要转换成str
#     response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
#     print(req)       # 打印请求报文
#     print('***************--下面是返回的报文******************')
#     print(response)  # 打印返回报文
