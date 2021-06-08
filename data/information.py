# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import os
import xlrd
from collections import defaultdict

fechii_content_cas = xlrd.open_workbook(".\原料总表FECHII.xlsx")
sheets_object = fechii_content_cas.sheets()
sheet_object = fechii_content_cas.sheet_by_index(0)
col_values_0 = sheet_object.col_values(colx=0)
col_values_1 = sheet_object.col_values(colx=1)
col_values_2 = sheet_object.col_values(colx=2)
col_values_6 = sheet_object.col_values(colx=6)
col_values_4 = sheet_object.col_values(colx=4)
col_values_5 = sheet_object.col_values(colx=5)
Data = []
for english, k3, chinese, cas, price, state in list(zip(col_values_0, col_values_1, col_values_2, col_values_4, col_values_5, col_values_6)):
    Data.append({"K3": k3, "English":english, "Chinese": chinese, "CAS": cas, "Price": price, "State": state})
#print(Data[-1])

Data1 = []
fechii_content_price = xlrd.open_workbook(".\原料总表FECHII.xlsx")
sheets_object = fechii_content_price.sheets()
sheet_object = fechii_content_price.sheet_by_index(1)
col_values_0 = sheet_object.col_values(colx=0)
col_values_1 = sheet_object.col_values(colx=1)
col_values_2 = sheet_object.col_values(colx=2)
col_values_3 = sheet_object.col_values(colx=3)
col_values_4 = sheet_object.col_values(colx=4)
col_values_5 = sheet_object.col_values(colx=5)
col_values_6 = sheet_object.col_values(colx=6)
col_values_7 = sheet_object.col_values(colx=7)
for k3, english, chinese, cas, price, state in list(zip(col_values_0, col_values_1, col_values_3, col_values_5, col_values_6, col_values_7)):
    Data1.append({"K3": k3, "English": english, "Chinese": chinese, "CAS": cas, "Price": price, "State": state})
#print(Data1[-1])

#print(len(Data), len(Data1))
#Data2 = Data+Data1

#CASNUM = []
#for i in Data2:
#    CASNUM.append(i['CAS'])
#print(CASNUM)

Data2 = []
fechii_content_original = xlrd.open_workbook(".\价格表(调香部专用)FECHII.xls")
sheets_object = fechii_content_original.sheets()
sheet_object = fechii_content_original.sheet_by_index(0)
col_values_0 = sheet_object.col_values(colx=0)
col_values_1 = sheet_object.col_values(colx=1)
col_values_2 = sheet_object.col_values(colx=2)
col_values_3 = sheet_object.col_values(colx=3)
col_values_4 = sheet_object.col_values(colx=4)

for k3, chinese, english, cas, price in list(zip(col_values_0, col_values_1,col_values_2,col_values_3, col_values_4)):
    Data2.append({"K3": k3, "English": english, "Chinese": chinese, "CAS": cas, "Price": price, "State": ''})

#print(Data2)

TotalData =  Data2
#print(TotalData)
TotalCAS = []
for index, item in list(enumerate(TotalData)):
    TotalCAS.append(item['CAS'])


