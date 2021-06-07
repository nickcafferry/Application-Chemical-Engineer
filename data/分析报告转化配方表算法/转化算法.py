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


Percent_Total = 0
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
    csv_to_xls(".\输入表格\%s"%csvfilenames[i], ".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))
    print("转化成功，目标文件为%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))
    print('---------------------------------------------------')
    print('\n')

for i in range(csvfnamelength):
    workbook_csv = xlrd.open_workbook(".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"),formatting_info=True)
    sheets_object_csv = workbook_csv.sheets()
    sheet_object_csv = workbook_csv.sheet_by_index(0)
    csv_excel = copy(workbook_csv)
    csv_sheet = csv_excel.get_sheet(0)
    insertcolno = 4
    if sheet_object_csv.cell(4, 0).value != "2=":
        csv_sheet.write(4, 0, "2=")
        csv_sheet.write(4, 1, "INT TIC: "+(sheet_object_csv.cell(2, 1).value.split("\\"))[-1]+"\data.ms")
        for RowIndex in range(insertcolno, sheet_object_csv.nrows):
            for colIndex in range(sheet_object_csv.ncols):
                csv_sheet.write(RowIndex+1, colIndex, sheet_object_csv.cell(RowIndex, colIndex).value)
    csv_excel.save(".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))


for i in range(csvfnamelength):
    workbook_csv = xlrd.open_workbook(".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"),formatting_info=True)
    sheets_object = workbook_csv.sheets()
    sheet_object_write = workbook_csv.sheet_by_index(0)
    csv_excel = copy(workbook_csv)
    csv_sheet = csv_excel.get_sheet(0) 
    insertrow = 5
    print(sheet_object_write.ncols)
    if sheet_object_write.cell(7, 5).value != "Ref":
        csv_sheet.write(7,5,"Ref")
        for RowIndex in range(insertrow, sheet_object_write.ncols):
            for ColIndex in range(sheet_object_write.nrows-7):
                csv_sheet.write(ColIndex+7,5," ")
                #csv_sheet.write(colIndex+1, RowIndex+1, sheet_object.cell(colIndex+1, RowIndex).value)
        for rowindex in range(sheet_object_write.nrows-7):
            csv_sheet.write(rowindex+7, 6, sheet_object_write.cell(rowindex+7, 5).value)
            csv_sheet.write(rowindex+7, 7, sheet_object_write.cell(rowindex+7, 6).value)
    csv_excel.save(".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))


#从输入表格中寻找CAS列并做标记，读取文件中CAS号及Area Pct(面积百分比)信息
CAS_REAL= []
AREA_REAL = []
for i in range(csvfnamelength):
    workbook1 = xlrd.open_workbook(".\输入表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"),formatting_info=True)
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
    Limonene_Index = []
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
    print("%s中所有香精原料的总面积为%f"%(csvfilenames[i].rstrip(".csv").rstrip(".CSV"),TotalArea))
    if round(TotalArea) != 100:
        print("%s中所有香精原料的总面积可能存在问题"%(csvfilenames[i].rstrip(".csv").rstrip(".CSV")))
    CAS_REAL = CAS_REAL
    AREA_REAL = AREA_REAL
    #print(CAS_REAL)
    print("---------------------------------------------------\n")
    print("\n")
    for index, item in list(enumerate(CAS_REAL)):
        if "138-86-3" == item:
            Limonene_Index.append(index)
        else:
            pass
    #print(Limonene_Index)



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
    Cis_3_hexenyl_acetate_flag = 0
    Cis_3_hexenyl_acetate_index = []
    Terpineol_BP_Flag = 0
    if 'gamma-Terpineol' in LibID and 'alpha-Terpineol' in LibID and "乙位松油醇 $$beta-Terpineol $" in LibID:
        Terpineol_BP_Flag = 1
        print("配方中有90%可能存在松油醇B.P.，请再仔细检查")
    elif 'gamma-Terpineol' in LibID and 'alpha-Terpineol' in LibID and "乙位松油醇 $$beta-Terpineol $" not in LibID:
        print("配方中有50%可能存在松油醇B.P.，请再仔细检查")
    elif 'gamma-Terpineol' in LibID and '乙位松油醇 $$beta-Terpineol $' in LibID and 'alpha-Terpineol' not in LibID:
        print("配方中有50%可能存在松油醇B.P.，请再仔细检查")
    elif 'alpha-Terpineol' in LibID and 'beta-Terpineol' in LibID and 'gamma-Terpineol' not in LibID:
        print("配方中有50%可能存在松油醇B.P, 请再仔细检查")
    elif 'gamma-Terpineol' in LibID or 'alpha-Terpineol' in LibID or "乙位松油醇 $$beta-Terpineol $" in LibID:
        print("配方中有20%可能存在松油醇B.P, 请再仔细检查")
    #print(Cis_3_hexenyl_acetate_flag, Cis_3_hexenyl_acetate_index)
    for index, item in list(enumerate(LibID)):
        if "Cis-3-hexenyl acetate" in item:
            Cis_3_hexenyl_acetate_flag = 1
            Cis_3_hexenyl_acetate_index.append(index)
        else:
            pass

    Terpineol_BP_Index = []
    if Terpineol_BP_Flag == 1:
        for index, item in list(enumerate(LibID)):
            if "gamma-Terpineol" in item or "乙位松油醇 $$beta-Terpineol $" in item or 'alpha-Terpineol' in item:
                Terpineol_BP_Index.append(index)
            else:
                pass


    #保留时间
    RTID = []
    RTIDrownumber = 0
    RTIDcolnumber = 0
    for j in range(collength):
        row_values= sheet_object.row_values(rowx=j)
        if "RT" in row_values or "保留时间" in row_values:
            RTIDcolnumber = j
            print(RTIDcolnumber)
            for k, item in list(enumerate(row_values)):
                if "RT" in item or "保留时间" in item:
                    print(k, item)
                    RTIDrownumber = k
    col_values_RT = sheet_object.col_values(colx=RTIDrownumber)
    print(col_values_RT)
    #print(RTIDcolnumber)
    nonerownumber = 0
    for m, everyitem in list(enumerate(col_values_0)):
        if "INT TIC" in everyitem:
            nonerownumber = m
            break
        else:
            nonerownumber= collength
    RTID = col_values_RT[RTIDcolnumber+1:nonerownumber]
    #print(nonerownumber,RTIDcolnumber)
    #print(RTID)  

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
            if Cis_3_hexenyl_acetate_flag == 0:
                new_sheet.write(index+2,8,LibID[index], style=styleOK)
                new_sheet.write(index+2,0, index+2,style=styleOK)
                new_sheet.write(index+2,1, '',style=styleOK)
                new_sheet.write(index+2,7, '',style=styleOK)
                new_sheet.write(index+2,1, RTID[index],style=styleOK)
        for data in information.TotalData:
            if everycas in data['CAS'] and "8000-41-7" not in everycas and "138-86-3" not in everycas:
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
                new_sheet.write(index+2,1, RTID[index],style=styleOK)
                break
            elif Terpineol_BP_Flag==1 and "8000-41-7" in everycas:
                new_sheet.write(index+2,8, 'TERPINEOL BP', style=styleOK)
                new_sheet.write(index+2,10, 46, style=styleOK)
                new_sheet.write(index+2,5, "松油醇B.P.", style=styleOK)
                new_sheet.write(index+2,4, "96032",style=styleOK)
                new_sheet.write(index+2,2, "96032", style=styleOK)
                new_sheet.write(index+2,3, "TERPINEOL BP",style=styleOK)
                new_sheet.write(index+2, 11, round(float(float(46)*float(AREA_REAL[index])),3), style=styleOK)
                new_sheet.write(index+2,0, index+2, style=styleOK)
                new_sheet.write(index+2,1, '', style=styleOK)
                new_sheet.write(index+2,7, '', style=styleOK)
                new_sheet.write(index+2,1, RTID[index],style=styleOK)
                break
            elif "138-86-3" in everycas:
                new_sheet.write(index+2,8, "D-LIMONENE", style=styleOK)
                new_sheet.write(index+2,10, 50, style=styleOK)
                new_sheet.write(index+2,5, "D-柠烯（96%)", style=styleOK)
                new_sheet.write(index+2,4, "93056",style=styleOK)
                new_sheet.write(index+2,2, "93056",style=styleOK)
                new_sheet.write(index+2,3, "D-LIMONENE",style=styleOK) 
                new_sheet.write(index+2, 11, round(float(float(50)*float(AREA_REAL[index])),3), style=styleOK)
                new_sheet.write(index+2,0, index+2, style=styleOK)
                new_sheet.write(index+2,1, '', style=styleOK)
                new_sheet.write(index+2,7, '', style=styleOK)
                new_sheet.write(index+2,1, RTID[index],style=styleOK)  
                new_sheet.write(index+2, 9, "7705-14-8", style=styleOK)              
            else:
                if Cis_3_hexenyl_acetate_index != []:
                    for libindex in Cis_3_hexenyl_acetate_index:
                        if libindex != index:
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
                            new_sheet.write(index+2,1, RTID[index],style=styleOK)
                        elif libindex == index:
                            new_sheet.write(index+2,8, "CIS 3 HEXENYL ACETATE", style=styleOK)
                            new_sheet.write(index+2,10, 520, style=styleOK)
                            new_sheet.write(index+2,5, "乙酸叶醇酯", style=styleOK)
                            new_sheet.write(index+2,4, "92043",style=styleOK)
                            new_sheet.write(index+2,2, "92043",style=styleOK)
                            new_sheet.write(index+2,3, "CIS 3 HEXENYL ACETATE",style=styleOK) 
                            new_sheet.write(index+2, 11, round(float(float(520)*float(AREA_REAL[index])),3), style=styleOK)
                            new_sheet.write(index+2,0, index+2, style=styleOK)
                            new_sheet.write(index+2,1, '', style=styleOK)
                            new_sheet.write(index+2,7, '', style=styleOK)
                            new_sheet.write(index+2,1, RTID[index],style=styleOK)
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
                    new_sheet.write(index+2,1, RTID[index],style=styleOK)

                
            for libindex in Terpineol_BP_Index:
                if libindex == index:
                    new_sheet.write(index+2,8, 'TERPINEOL BP', style=styleOK)
                    new_sheet.write(index+2,10, 46, style=styleOK)
                    new_sheet.write(index+2,5, "松油醇B.P.", style=styleOK)
                    new_sheet.write(index+2,4, "96032",style=styleOK)
                    new_sheet.write(index+2,2, "96032", style=styleOK)
                    new_sheet.write(index+2,3, "TERPINEOL BP",style=styleOK)
                    new_sheet.write(index+2, 11, round(float(float(46)*float(AREA_REAL[index])),3), style=styleOK)
                    new_sheet.write(index+2,0, index+2, style=styleOK)
                    new_sheet.write(index+2,1, '', style=styleOK)
                    new_sheet.write(index+2,7, '', style=styleOK)
                    new_sheet.write(index+2,1, RTID[index],style=styleOK)

        if Cis_3_hexenyl_acetate_index != []:
            for libindex in Cis_3_hexenyl_acetate_index:
                if libindex != index:
                    new_sheet.write(index+2, 9, everycas, style=styleOK)
                elif libindex == index:
                    new_sheet.write(index+2, 9, "3681-71-8", style=styleOK)
        else:
            new_sheet.write(index+2, 9, everycas, style=styleOK)


    for key, percent in list(enumerate(AREA_REAL)):
        new_sheet.write(key+2, 6, round(percent,3), style=styleOK)
        new_sheet.write(key+2, 0, key+1, style=styleOK)
    #new_excel.save(".\输出表格\%s.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))





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

    Price_Total = 0

    for index, everyitem in list(enumerate(formula_CAS)):
        for data in information.TotalData:
            if everyitem[-1] in data['CAS'] and "138-86-3" not in everyitem[-1]:
                formula_sheet.write(index+2,8, data['English'], style=styleOK)
                formula_sheet.write(index+2,10, data['Price'], style=styleOK)
                formula_sheet.write(index+2,5, data["Chinese"], style=styleOK)
                formula_sheet.write(index+2,4, data["K3"],style=styleOK)
                formula_sheet.write(index+2,2, data["K3"], style=styleOK)
                formula_sheet.write(index+2,3, data["English"],style=styleOK)
                formula_sheet.write(index+2,1, RTID[everyitem[0]],style=styleOK)
                try:
                    formula_sheet.write(index+2, 11, round(float(float(data["Price"])*float(AREA_REAL[everyitem[0]]/1)),3), style=styleOK)
                    Price_Total = Price_Total+round(float(float(data["Price"])*float(AREA_REAL[everyitem[0]]/1)),3)
                except:
                    formula_sheet.write(index+2, 11, "Please Check", style=styleOK)
               # formula_sheet.write(index+2,0, index+2,style=styleOK)
                #formula_sheet.write(index+2,1, '',style=styleOK)
                formula_sheet.write(index+2,7, '',style=styleOK)
            
            elif everyitem[-1] in data['CAS'] and "138-86-3" in everyitem[-1]:
                formula_sheet.write(index+2,8, 'D-LIMONENE', style=styleOK)
                formula_sheet.write(index+2,10, 50, style=styleOK)
                formula_sheet.write(index+2,5, "D-柠烯（96%）", style=styleOK)
                formula_sheet.write(index+2,4, "93056",style=styleOK)
                formula_sheet.write(index+2,2, "93056", style=styleOK)
                formula_sheet.write(index+2,3, "D-LIMONENE",style=styleOK)
                formula_sheet.write(index+2, 11, round(float(float(50)*float(AREA_REAL[everyitem[0]])),3), style=styleOK)
                formula_sheet.write(index+2,0, index+2, style=styleOK)
                formula_sheet.write(index+2,1, '', style=styleOK)
                formula_sheet.write(index+2,7, '', style=styleOK)
                formula_sheet.write(index+2,1, RTID[everyitem[0]],style=styleOK)
                formula_sheet.write(index+2, 9, "7705-14-8", style=styleOK)     
                try:
                    Price_Total = Price_Total+round(float(float(50)*float(AREA_REAL[everyitem[0]]/1)),3)
                except:
                    print("价格表存在问题")            

            else:
                for libindex in Cis_3_hexenyl_acetate_index:
                    if libindex == index and "138-86-3" not in formula_CAS[index]:
                        formula_sheet.write(index+2,8, "CIS 3 HEXENYL ACETATE", style=styleOK)
                        formula_sheet.write(index+2,10, 520, style=styleOK)
                        formula_sheet.write(index+2,5, "乙酸叶醇酯", style=styleOK)
                        formula_sheet.write(index+2,4, "92043",style=styleOK)
                        formula_sheet.write(index+2,2, "92043",style=styleOK)
                        formula_sheet.write(index+2,3, "CIS 3 HEXENYL ACETATE",style=styleOK) 
                        formula_sheet.write(index+2, 11, round(float(float(520)*float(AREA_REAL[everyitem[0]])),3), style=styleOK)
                        formula_sheet.write(index+2,0, index+2, style=styleOK)
                        formula_sheet.write(index+2,1, '', style=styleOK)
                        formula_sheet.write(index+2,7, '', style=styleOK)
                        formula_sheet.write(index+2,1, RTID[everyitem[0]],style=styleOK)
                        try:
                            Price_Total = Price_Total+round(float(float(520)*float(AREA_REAL[everyitem[0]]/1)),3)
                        except:
                            print("价格表存在问题")                                

                for libindex in Terpineol_BP_Index:
                    if libindex == index and "138-86-3" not in formula_CAS[index]:
                        formula_sheet.write(index+2,8, 'TERPINEOL BP', style=styleOK)
                        formula_sheet.write(index+2,10, 46, style=styleOK)
                        formula_sheet.write(index+2,5, "松油醇B.P.", style=styleOK)
                        formula_sheet.write(index+2,4, "96032",style=styleOK)
                        formula_sheet.write(index+2,2, "96032", style=styleOK)
                        formula_sheet.write(index+2,3, "TERPINEOL BP",style=styleOK)
                        formula_sheet.write(index+2, 11, round(float(float(46)*float(AREA_REAL[everyitem[0]])),3), style=styleOK)
                        formula_sheet.write(index+2,0, index+2, style=styleOK)
                        formula_sheet.write(index+2,1, '', style=styleOK)
                        formula_sheet.write(index+2,7, '', style=styleOK)
                        formula_sheet.write(index+2,1, RTID[everyitem[0]],style=styleOK)
                        try:
                            Price_Total = Price_Total+round(float(float(46)*float(AREA_REAL[everyitem[0]]/1)),3)
                        except:
                            print("价格表存在问题")  
        
        if Cis_3_hexenyl_acetate_index != [] and "138-86-3" not in formula_CAS[index]:
            for libindex in Cis_3_hexenyl_acetate_index:
                if libindex != index and "138-86-3" not in formula_CAS[index]:
                    formula_sheet.write(index+2, 9, formula_CAS[index][-1], style=styleOK)
                elif libindex == index:
                    formula_sheet.write(index+2, 9, "3681-71-8", style=styleOK)
        elif "138-86-3" not in formula_CAS[index]:
            formula_sheet.write(index+2, 9, formula_CAS[index][-1], style=styleOK)
                 
        for libindex in Terpineol_BP_Index:
            if libindex == index and "138-86-3" not in formula_CAS[index]:
                formula_sheet.write(index+2, 9, "8000-41-7", style=styleOK)

                 
        formula_sheet.write(index+2, 6, round(float(AREA_REAL[everyitem[0]]/1),3), style=styleOK)
        formula_sheet.write(index+2, 0, index+1, style=styleOK)
    
    styleOK1 = xlwt.easyxf()
 
    pattern1 = xlwt.Pattern()  # 一个实例化的样式类
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
    pattern.pattern_fore_colour = xlwt.Style.colour_map['white']  # 背景颜色
 
    borders1 = xlwt.Borders()  # 为样式创建边框
    borders1.left = 1
    borders1.right = 1
    borders1.top = 1
    borders1.bottom =1
 
    font1 = xlwt.Font()  # 为样式创建字体
    font1.name = '华文中宋'
    font1.bold = True
    font1.height = 240
    
    styleOK1.pattern = pattern1
    styleOK1.borders = borders1
    styleOK1.font = font1


    TitleInfo = "%s" %csvfilenames[i].rstrip(".csv").rstrip(".CSV").split("(")[0]
    styleOK2 = xlwt.easyxf()
 
    pattern2 = xlwt.Pattern()  # 一个实例化的样式类
    pattern2.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
    pattern2.pattern_fore_colour = xlwt.Style.colour_map['white']  # 背景颜色
 
    borders2 = xlwt.Borders()  # 为样式创建边框
    borders2.left = 1
    borders2.right = 1
    borders2.top = 1
    borders2.bottom =1
 
    font2 = xlwt.Font()  # 为样式创建字体
    font2.name = '华文中宋'
    font2.bold = True
    font2.height = 480
    
    styleOK2.pattern = pattern2
    styleOK2.borders = borders2
    styleOK2.font = font2

    userinfo = os.getlogin()

    formula_sheet.write_merge(0, 0, 6, 7, round(float(Price_Total/100),3), style=styleOK1)
    formula_excel.save(".\输出表格\%s-已处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))
    new_sheet.write_merge(0, 0, 6, 7, round(float(Price_Total/100),3), style=styleOK1)
    new_excel.save(".\输出表格\%s-未处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))        


    workbook_price = xlrd.open_workbook(".\输出表格\%s-已处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"),formatting_info=True)
    sheets_object_price = workbook1.sheets()
    sheet_object_price = workbook_price.sheet_by_index(0)
    col_values_price = sheet_object_price.col_values(colx=11)
    col_values_percent = sheet_object_price.col_values(colx=6)
    Price_Total=sum(col_values_price[2:])
    Percent_Total= sum(col_values_percent[2:])
    #print(Price_Total)

    price_excel = copy(workbook_price)
    price_sheet = price_excel.get_sheet(0)
    price_sheet.write_merge(0, 0, 6, 7, round(float(Price_Total/Percent_Total),3), style=styleOK1)
    price_sheet.write_merge(0, 0, 0, 5, TitleInfo, style=styleOK2)
    price_sheet.write_merge(0, 0, 9, 11, "分析人："+userinfo, style=styleOK2)
    price_excel.save(".\输出表格\%s-已处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))

    workbook_price_unchanged = xlrd.open_workbook(".\输出表格\%s-未处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"),formatting_info=True)
    price_excel = copy(workbook_price_unchanged)
    price_sheet = price_excel.get_sheet(0)
    price_sheet.write_merge(0, 0, 6, 7, round(float(Price_Total/Percent_Total),3), style=styleOK1)
    price_sheet.write_merge(0, 0, 0, 5, TitleInfo, style=styleOK2)
    price_sheet.write_merge(0, 0, 9, 11, "分析人："+userinfo, style=styleOK2)
    price_excel.save(".\输出表格\%s-未处理配方.xls"%csvfilenames[i].rstrip(".csv").rstrip(".CSV"))

print("\n")
print("===============================")
print("配方已经全部处理完，算法运行结束")
print("===============================")
