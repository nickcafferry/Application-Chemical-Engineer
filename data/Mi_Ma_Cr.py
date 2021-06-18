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
import xlrd
from xlutils.copy import copy
import xlwt 
import os

def set_style(name, height, bold=False, format_str='',align='center'):
    style = xlwt.XFStyle()  # 初始化样式
 
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.height = height
 
    borders = xlwt.Borders()  # 为样式创建边框
    borders.left = 2
    borders.right = 2
    borders.top = 0
    borders.bottom = 2
 
    alignment = xlwt.Alignment()  # 设置排列
    if align== 'center':
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
    else:
        alignment.horz = xlwt.Alignment.HORZ_LEFT
        alignment.vert = xlwt.Alignment.VERT_BOTTOM
 
    style.font = font
    style.borders = borders
    style.num_format_str = format_str
    style.alignment = alignment
 
    return style

styleOK = xlwt.easyxf()
 
pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 背景颜色
 
borders = xlwt.Borders()  # 为样式创建边框
borders.left = 2
borders.right = 2
borders.top = 6
borders.bottom = 2
 
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True
font.height = 220
 
styleOK.pattern = pattern
styleOK.borders = borders
styleOK.font = font

styleOK1 = xlwt.easyxf()
 
pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['green']  # 背景颜色
 
borders = xlwt.Borders()  # 为样式创建边框
borders.left = 2
borders.right = 2
borders.top = 6
borders.bottom = 2
 
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True
font.height = 220
 
styleOK1.pattern = pattern
styleOK1.borders = borders
styleOK1.font = font

styleOK2 = xlwt.easyxf()
 
pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['red']  # 背景颜色
 
borders = xlwt.Borders()  # 为样式创建边框
borders.left = 2
borders.right = 2
borders.top = 6
borders.bottom = 2
 
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True
font.height = 220
 
styleOK2.pattern = pattern
styleOK2.borders = borders
styleOK2.font = font



workbook = xlrd.open_workbook("1.xlsx")
sheet1_object = workbook.sheet_by_index(0)
col_values = sheet1_object.col_values(colx=20)

workbook2 = xlwt.Workbook(encoding='utf-8')
worksheet2 = workbook2.add_sheet('异常')

length = len(col_values)

for index, item in list(enumerate(sheet1_object.row_values(rowx=0))):
    worksheet2.write(0, index, sheet1_object.row_values(rowx=0)[index])

for index, item in list(enumerate(col_values)):
    if item == "Cr":
        row_values = sheet1_object.row_values(rowx=index)
        for key, item in list(enumerate(row_values)):
            worksheet2.write(index, key, row_values[key],style=styleOK)
    if item == "Mi":
        row_values = sheet1_object.row_values(rowx=index)
        for key, item in list(enumerate(row_values)):
            worksheet2.write(index, key, row_values[key],style=styleOK1)
    if item == "Ma":
        row_values = sheet1_object.row_values(rowx=index)
        for key, item in list(enumerate(row_values)):
            worksheet2.write(index, key, row_values[key],style=styleOK2)


workbook2.save('KPI.xls')







