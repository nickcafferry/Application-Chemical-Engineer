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


with open("output.txt", 'w', encoding="utf-8") as output:
    with open("xifashui01.html", 'r', encoding="utf-8") as f:
        print(f.read(), file=output)
        
with open("output.txt", 'r', encoding="utf-8") as output0:
    lengthofzhiyu = len(output0.readlines())

output1 = open("output.txt", 'r', encoding="utf-8")

productTitle = []
productStatus = []

for i in range(lengthofzhiyu):
    targetline = output1.readline()
    if '<p class="productTitle">' in targetline:
        targetline = output1.readline()
        targetline = output1.readline()
        targetline = output1.readline()
        productTitle.append(targetline.replace("<span class=H>", '').replace("</span>", '').replace(' ', ''))
    elif '<p class="productStatus" >' in targetline:
        targetline = output1.readline()
        productStatus.append(targetline.split('>')[-3].rstrip('笔</em'))
        
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('xifashui_P1-TMall')

for i in range(len(productTitle)):
    worksheet.write(i,0, productTitle[i])

for s in range(len(productStatus)):
    worksheet.write(s, 1, productStatus[s])

workbook.save('xifashui_P1-TMall.xls')


