# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import os
import xlrd
from xlutils.copy import copy
import xlwt
import re
import urllib.request as ur
import requests
import urllib
import json
from xlwt.Workbook import Workbook
import xlwt 
from csv2excel import csv_to_xls
import information
from xlwt import easyxf
from xlutils.styles import Styles

def set_style(name, height, bold=False, format_str='',align='center'):
    style = xlwt.XFStyle()  # 初始化样式
 
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.height = height
 
    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
 
    alignment = xlwt.Alignment()  # 设置排列
    if align== 'center':
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
    else:
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
 
    style.font = font
    style.borders = borders
    style.num_format_str = format_str
    style.alignment = alignment
 
    return style

styleOK = xlwt.easyxf()
 
pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['white']  # 背景颜色
 
borders = xlwt.Borders()  # 为样式创建边框
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom =1
 
font = xlwt.Font()  # 为样式创建字体
font.name = '华文中宋'
font.bold = False
font.height = 240
 
styleOK.pattern = pattern
styleOK.borders = borders
styleOK.font = font


#检测输入表格并计算它们的数量
filenames = []
outputdir = ".\输入表格"
for item in os.listdir(outputdir):
    if item.split('.')[-1] != 'py' and item.split('.')[-1] == 'xlsx' or item.split('.')[-1] == 'csv' and os.path.isdir(item) == False or item.split('.')[-1] == 'xls':
        filenames.append(item)
    else: 
        pass
#print(filenames)
fnamelength = len(filenames)
#print(fnamelength)



#检测输入表格的格式，如果是".csv"文件, 则识别为RESULTS.csv文件
csvfilenames = []
for item in os.listdir(outputdir):
    if item.split('.')[-1] != 'py' and item.split('.')[-1] != 'xlsx' and item.split('.')[-1] == 'csv' or item.split('.')[-1] == 'CSV' and os.path.isdir(item) == False and item.split('.')[-1] != 'xls':
        csvfilenames.append(item)
    else: 
        pass
#print(csvfilenames)
csvfnamelength = len(csvfilenames)
#print(csvfnamelength)
for i in range(csvfnamelength):
    print("csv转excel算法正在转化%s文件..."%(csvfilenames[i]))
    print('----------------------------------------------------')
    csv_to_xls(".\输入表格\%s"%csvfilenames[i], ".\输入表格\%s.xls"%csvfilenames[i].strip(".csv").strip(".CSV"))
    print("转化成功，目标文件为%s.xls"%csvfilenames[i].strip(".csv").strip(".CSV"))
    print('---------------------------------------------------')
    print('\n')

#从输入表格中寻找CAS列并做标记，读取文件中CAS号及Area Pct(面积百分比)信息
CAS_REAL= []
AREA_REAL = []
for i in range(csvfnamelength):
    workbook1 = xlrd.open_workbook(".\输入表格\%s.xls"%csvfilenames[i].strip(".csv").strip(".CSV"),formatting_info=True)
    sheets_object = workbook1.sheets()
    sheet_object = workbook1.sheet_by_index(0)
    col_values_0 = sheet_object.col_values(colx=0)
    collength = len(col_values_0)
    casrownumber = 0
    cascolnumber = 0

    #CAS号
    for j in range(collength):
        row_values= sheet_object.row_values(rowx=j)
        if "CAS" in row_values:
            cascolnumber = j
            for k, item in list(enumerate(row_values)):
                if "CAS" in item:
                    #print(k, item)
                    casrownumber = k
    col_values = sheet_object.col_values(colx=casrownumber)

    nonerownumber = 0
    for l, item in list(enumerate(col_values_0)):
        if "INT TIC" in item:
            nonerownumber = l
            break
        else:
            nonerownumber= collength
    CAS_CONTENT = col_values[cascolnumber+1:nonerownumber]
    CAS_REAL = []
    for item in CAS_CONTENT:
        if item.startswith("0") and not item.endswith("-00-0"):
            item = item.lstrip("0")
            CAS_REAL.append(item)
        elif item == '' or item == ' ':
            CAS_REAL.append(item)
        elif item.endswith("-00-0"):
            CAS_REAL.append(item)
        else:
            CAS_REAL.append(item)
    #print(CAS_REAL)
    #print(len(CAS_REAL))
    
    #Area Pct或者面积百分比
    arearownumber = 0
    areacolnumber = 0
    for j in range(collength):
        row_values= sheet_object.row_values(rowx=j)
        if "Area Pct" in row_values or "面积百分比" in row_values:
            areacolnumber = j
            for k, item in list(enumerate(row_values)):
                if "Area Pct" in item or "面积百分比" in item:
                    #print(k, item)
                    arearownumber = k
    col_values_area = sheet_object.col_values(colx=arearownumber)
    #print(col_values_area)

    nonerownumber = 0
    for m, everyitem in list(enumerate(col_values_0)):
        if "INT TIC" in everyitem:
            nonerownumber = m
            break
        else:
            nonerownumber= collength
    AREA_CONTENT = col_values_area[areacolnumber+1:nonerownumber]
    AREA_REAL = []
    for area in AREA_CONTENT:
        AREA_REAL.append(float(area.strip(' ')))
    
    TotalArea = 0
    print("----------------------------------------------------")
    for num, everyarea in list(enumerate(AREA_REAL)):
        if everyarea < 0:
            print("第%d行存在负数面积百分比"%(num+1))
            feedback = input("请问需要清零吗?: (y/n) \n")
            if feedback == "y" or feedback == "Y":
                print("执行清零算法...")
                AREA_REAL[num] = 0
            elif feedback == "n" or feedback == "N":
                pass
            else:
                print("请输入Y/N, 或y/n")
        else:
            pass
    print("面积百分比数据已经全部格式化...")
    for everyarea in AREA_REAL:
        TotalArea = TotalArea+everyarea
    print("%s中所有香精原料的总面积为%f"%(csvfilenames[i].strip(".csv").strip(".CSV"),TotalArea))
    if int(TotalArea) != 100:
        print("%s中所有香精原料的总面积可能存在问题"%(csvfilenames[i].strip(".csv").strip(".CSV")))
    CAS_REAL = CAS_REAL
    AREA_REAL = AREA_REAL
    #print(CAS_REAL)
    print("---------------------------------------------------\n")
    print("\n")



    #Library ID
    LibID = []
    LibIDrownumber = 0
    LibIDcolnumber = 0
    for j in range(collength):
        row_values= sheet_object.row_values(rowx=j)
        if "Library/ID" in row_values or "/ID" in row_values:
            LibIDcolnumber = j
            for k, item in list(enumerate(row_values)):
                if "Library/ID" in item or "/ID" in item:
                    print(k, item)
                    LibIDrownumber = k
    col_values_lib = sheet_object.col_values(colx=LibIDrownumber)
    #print(col_values_lib)
    nonerownumber = 0
    for m, everyitem in list(enumerate(col_values_0)):
        if "INT TIC" in everyitem:
            nonerownumber = m
            break
        else:
            nonerownumber= collength
    LibID = col_values_lib[LibIDcolnumber+1:nonerownumber]
    #print(LibID)




    #创建对应的模板表格
    workbook = xlrd.open_workbook(".\空白配方转化表FECHII_TEST.xls", formatting_info=True)
    table = workbook.sheet_by_index(0)
    styles = Styles(workbook)
    sheets_object = workbook.sheets()
    sheet1_object = workbook.sheet_by_index(0)
    col_values = sheet1_object.col_values(colx=9)
    #print(col_values)
    #collength = len(CAS_REAL)
    new_excel = copy(workbook)
    new_sheet = new_excel.get_sheet(0)
    for index, everycas in list(enumerate(CAS_REAL)):
        if everycas == '' or everycas.endswith("-00-0"):
            new_sheet.write(index+2,8,LibID[index], style=styleOK)
            new_sheet.write(index+2,0, index+2,style=styleOK)
            new_sheet.write(index+2,1, '',style=styleOK)
            new_sheet.write(index+2,7, '',style=styleOK)
        for data in information.TotalData:
            if everycas in data['CAS']:
                new_sheet.write(index+2,8, data['English'], style=styleOK)
                new_sheet.write(index+2,10, data['Price'], style=styleOK)
                new_sheet.write(index+2,5, data["Chinese"], style=styleOK)
                new_sheet.write(index+2,4, data["K3"],style=styleOK)
                new_sheet.write(index+2,2, data["K3"], style=styleOK)
                new_sheet.write(index+2,3, data["English"],style=styleOK)
                new_sheet.write(index+2, 11, round(float(float(data["Price"])*float(AREA_REAL[index])),3), style=styleOK)
                new_sheet.write(index+2,0, index+2, style=styleOK)
                new_sheet.write(index+2,1, '', style=styleOK)
                new_sheet.write(index+2,7, '', style=styleOK)
                break
            else:
                new_sheet.write(index+2,8,LibID[index], style=styleOK)
                new_sheet.write(index+2,10, 'unknown', style=styleOK)
                new_sheet.write(index+2,5, 'unknown', style=styleOK)
                new_sheet.write(index+2,4, 'unknown', style=styleOK)
                new_sheet.write(index+2,2, 'unknown', style=styleOK)
                new_sheet.write(index+2,3, 'unknown', style=styleOK)
                new_sheet.write(index+2, 11, "unknown", style=styleOK)
                new_sheet.write(index+2,0, index+2,style=styleOK)
                new_sheet.write(index+2,1, '',style=styleOK)
                new_sheet.write(index+2,7, '',style=styleOK)
        new_sheet.write(index+2, 9, everycas, style=styleOK)
    for key, percent in list(enumerate(AREA_REAL)):
        new_sheet.write(key+2, 6, round(percent,3), style=styleOK)
        new_sheet.write(key+2, 0, key+1, style=styleOK)
    new_excel.save(".\输出表格\%s.xls"%csvfilenames[i].strip(".csv").strip(".CSV"))

    formula_excel = copy(workbook)
    formula_sheet = formula_excel.get_sheet(0)
    formula_CAS = []
    for index, everycas in list(enumerate(CAS_REAL)):
        if everycas == '' or everycas.endswith("-00-0"):
            pass
        for data in information.TotalData:
            if everycas in data['CAS']:
                formula_CAS.append([index,everycas])
                break
            else:
                pass
    Area_Total = 0
    for formula in formula_CAS:
        Area_Total += AREA_REAL[formula[0]]
    for index, everyitem in list(enumerate(formula_CAS)):
        for data in information.TotalData:
            if everyitem[-1] in data['CAS']:
                formula_sheet.write(index+2,8, data['English'], style=styleOK)
                formula_sheet.write(index+2,10, data['Price'], style=styleOK)
                formula_sheet.write(index+2,5, data["Chinese"], style=styleOK)
                formula_sheet.write(index+2,4, data["K3"],style=styleOK)
                formula_sheet.write(index+2,2, data["K3"], style=styleOK)
                formula_sheet.write(index+2,3, data["English"],style=styleOK)
                try:
                    formula_sheet.write(index+2, 11, round(float(float(data["Price"])*float(AREA_REAL[everyitem[0]]/1)),3), style=styleOK)
                except:
                    formula_sheet.write(index+2, 11, "Please Check", style=styleOK)
               # formula_sheet.write(index+2,0, index+2,style=styleOK)
                formula_sheet.write(index+2,1, '',style=styleOK)
                formula_sheet.write(index+2,7, '',style=styleOK)
        formula_sheet.write(index+2, 9, formula_CAS[index][-1], style=styleOK)
        formula_sheet.write(index+2, 6, round(float(AREA_REAL[everyitem[0]]/1),3), style=styleOK)
        formula_sheet.write(index+2, 0, index+1, style=styleOK)

    formula_excel.save(".\输出表格\%s-检测.xls"%csvfilenames[i].strip(".csv").strip(".CSV"))

        
    


















#检测输入表格的格式，如果是".xls"或者".xls"文件, 则识别为RESULTS.xls文件

csvfilenames = []

for item in os.listdir(outputdir):
    if item.split('.')[-1] != 'py' and item.split('.')[-1] != 'xlsx' and item.split('.')[-1] == 'csv' or item.split('.')[-1] == 'CSV' and os.path.isdir(item) == False and item.split('.')[-1] != 'xls':
        csvfilenames.append(item)
    else: 
        pass
print(csvfilenames)
csvfnamelength = len(csvfilenames)
print(csvfnamelength)







