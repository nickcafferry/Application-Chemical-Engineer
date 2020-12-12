#!/usr/local/bin/python

import urllib.request as ur
import os

response = input("Please text Fircom Asp ID number: \n")
response = "http://erp.zoteq.com:81/bdzy/ecata/FIRCOM_V.ASP?id="+str(response)
response0 = ur.urlopen(response)
response1 = ur.urlopen(response)


# Find the filename
for everyline in range(len(response0.readlines())):
	try:
		line = response1.readline().decode('utf-8')
	except:
		pass

	if 'font face="Verdana" style="font-size: 14pt"' in line:
		filename = response1.readline().decode('utf-8').split('&')[0].lstrip('\t').rstrip('\n').rstrip('\r').rstrip('</td>').rstrip('</font>')
		print(filename)
		if ' ' in filename:
			namelist = filename.split(' ')
			filename = '-'.join(namelist)
			if '%' in filename:
				filename = filename.replace('%','')
		else:
			pass

# Recording html information
response0 = ur.urlopen(response)
response1 = ur.urlopen(response)
f = open("%s-org.html"%filename,'w',encoding="utf-8")
for everline in range(len(response0.readlines())):
	try:
		print(response1.readline().decode('gb2312'), file=f)
	except:
		print('\n', file=f)
f.close()
	
# Make changes to html file
f = open("%s-org.html"%filename,'r',encoding='utf-8')
content=f.readlines()
fwriter = open("target.html", 'w', encoding='utf-8')
for item in content:
	if 'img border="0" src=' or '|&nbsp;</font><a href=' in item:
		new = item.replace('..', 'http://erp.zoteq.com:81/bdzy')
		fwriter.write(new)
	else:
		fwriter.write(item)
fwriter.close()
os.system('rename target.html %s.html'%filename)
os.system('notepad.exe %s.html'%filename)
os.system('"F:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://github.com/nickcafferry/Fechii-Application-Chemical-Engineer/tree/master/doc/assets')
os.system('"F:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/%s.html'%filename)