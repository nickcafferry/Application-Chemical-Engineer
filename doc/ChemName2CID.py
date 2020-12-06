# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import urllib.request
import time
from urllib import request, parse

# establish an file for recording information
file = open("ChemNametoCID.txt", 'w', encoding='utf-8')
file.write("Chemical Name, PubChem CID\n")

#Read the file "fechiimaterials.html" and acquire the Puhchem link for every substance.

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}


i = 1
with open("fechiimaterials.html", 'r', encoding="utf-8") as f:
	for everyline in f.readlines():
		if """href="https://pubchem.ncbi.nlm.nih.gov/""" in everyline:
			targetline = everyline.split('>')[1].split('=')[-1]
			htmllink = targetline.rstrip('"').lstrip('"')
			print(htmllink)
			req = urllib.request.Request(url=htmllink, headers=headers, method='POST')
			try:
				response = urllib.request.urlopen(req)
				response1 = urllib.request.urlopen(req)

				if response.getcode() == "404":
					print(everyline.split('>')[-1].strip('</td>\n'))
					file.write("%s, None"%everyline.split('>')[-1].strip('</td>\n'))
				else: 
					for line in range(len(response.readlines())):
						targetline = response1.readline().decode('utf-8')
						if '    <meta property="og:title"' in targetline:
							chemname = targetline.split('=')[-1].rstrip('">\n').lstrip('"')
							print(chemname)

						if '    <meta property="og:url"' in targetline:
							targetcid = targetline.split('=')[-1].split('/')[-1][:-3]
							print(targetcid)
					
						
					file.write("%s, %s\n"%(chemname, targetcid))
				time.sleep(20)
			except:
				file.write("%s, HTTP Error!\n"%everyline.split('>')[-1].strip('</td>\n'))
	file.close()

				
#				with open(".\ChemName2CID\%s.html"%str(i), 'w', encoding="utf-8") as k:
#					for everyline in range(len(response.readlines())):
#						print(response1.readline().decode('utf-8'), file=k)
#				k.close()
#				i+=1			