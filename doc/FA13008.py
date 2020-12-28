#!/usr/local/bin/python

import urllib.request as ur
import os
import time
from urllib import request, parse

f = open("FA13008.csv", encoding="utf-8")
lenofcont = len(f.readlines())
print(lenofcont)

f = open("FA13008.csv", encoding="utf-8")
f.readline()
f.readline()
Dname = f.readline().split(',')[:8]
FADict = {}
FAList = []
for i in range(62):
	everyline = f.readline().split(',')[:8]
	FADict.update({Dname[0]:everyline[0]})
	FADict.update({Dname[1]:everyline[1]})
	FADict.update({Dname[2]:everyline[2]})
	FADict.update({Dname[3]:everyline[3]})
	FADict.update({Dname[4]:everyline[4]})
	FADict.update({Dname[5]:everyline[5]})
	FADict.update({Dname[6]:everyline[6]})
	FADict.update({Dname[7]:everyline[7]})
	FAList.append([FADict])
	FADict = {}
f.close()

CAS_List = []
for item in FAList:
	CAS_List.append(item[0]['CAS编号'])
print(CAS_List)	
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

html_list = []
for item in CAS_List:
	html='https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=csv&query={%22download%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22*%22:%22'+str(item)+'%22}]},%22order%22:[%22relevancescore,desc%22],%22start%22:1,%22limit%22:10000000,%22downloadfilename%22:%22PubChem_compound_text_'+str(item)+'%22}'
	html_list.append(html)

opfile = open("output.csv",'w',encoding='utf-8')
req = ur.Request(url=html_list[0], headers=headers, method='POST')
leaders = ur.urlopen(req).readline().decode('utf-8')
opfile.write(leaders)
print("Initialing", end='')
time.sleep(1)
print('.........',end='\n')



#leaders = leaders.split(',')
#leaders[0] = leaders[0].lstrip('\ufeff')
#leaders[-1]= leaders[-1].rstrip('\n')

i=0
for everyhtml in html_list:
	try:
		req = ur.Request(url=everyhtml, headers=headers, method='POST')
		response = ur.urlopen(req)
		if response.getcode() == "404":
			opfile.write('html page does not exist!\n')
		else:
			response.readline().decode('utf-8')
			content=response.readline().decode('utf-8')
			opfile.write(content)
			time.sleep(10)
	except:
		opfile.write("HTTP Error!\n")
	i += 1
	print('%s html is done, continuing......'%str(i))
#	if i == 3:
#		break
opfile.close()