# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from Color import *
import os
def HASH(s):
	L = '# '
	L = L + s
	if len(L) < 78:
		L = L + (78-len(L))*' '
	else:
		print('The length of the string given is no smaller than 78')
	L = L + '#'
	return L


f = open("RT-Database.html", 'r', encoding="utf-8")
content = f.readlines()
f = open("RT-Database.html", 'r', encoding="utf-8")
for i in range(100000):
	if f.readline() == '          <tr class="row2">\n':
		targetnum = i
		printYellowRed("找到目标所在的位置: 位于第 %s 行!\n"%(i+1))
		printBlue(u'--------------------------------------------------------------------------------\n')
		break

f = open("RT-Database.html", 'r', encoding="utf-8")
for j in range(i):
	f.readline()
printRed(u"读完目标前面的所有内容!\n")

printYellow(u"开始打印目标后9行内容: \n")
printBlue(u'--------------------------------------------------------------------------------\n')
printRed(u'###############################################################################\n')
for k in range(9):
	printYellowRed('%s\n'%f.readline())
printRed(u'###############################################################################\n')
targetnum = targetnum + 9

printRed(u"欢迎您开始正式工作: \n")

for x in range(10000000):
	printYellow(u"开始打印目标后9行内容: \n")
	printBlue(u'--------------------------------------------------------------------------------\n')
	printRed(u'###############################################################################\n')
	for y in range(9):
		printYellowRed('%s\n'%f.readline())
	printRed(u'###############################################################################\n')
#	Q1 = input('您是否想要在此处增加链接? 是(y or Y)/不是(n or N) \n')
	Q1 = 'y'
	if Q1 == 'y' or Q1 == 'Y':
		printYellow("好的, 正在处理... \n")
		productname = content[targetnum+4].split('>')[1].strip(' </td')
		target_string = content[targetnum+4].split('>')[0] + '>'+ """<a target="_blank" href="https://pubchem.ncbi.nlm.nih.gov/compound/%s"> """ % (productname) +content[targetnum+4].split('>')[1]+'>' +content[targetnum+4].split('>')[2]  
		content = content[:targetnum+4]+[target_string]+content[targetnum+5:]
		fwriter = open("target.html", 'w', encoding='utf-8')
		for everyline in content:
			fwriter.write(everyline)
	if productname == 'Cyclohexadecanolide':
		break

#		Q2 = input('您想结束本次使用吗? 是(y or Y)/不是(n or N) \n')
#		if Q2 == 'y' or Q2 == 'Y':
#			break
		
#	if Q1 == 'n' or Q1 == 'N':
#		Q2 = input('您想结束本次使用吗? 是(y or Y)/不是(n or N) \n')
#		if Q2 == 'y' or Q2 == 'Y':
#			break
#		continue
	
	
	targetnum = targetnum + 9
	
	fwriter.close()
