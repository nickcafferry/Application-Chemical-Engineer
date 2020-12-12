#!/usr/local/bin/python
f = open("index.md", "w") 
f1 = open('Conformer3D_CID_61014.sdf')
for i in range(400):
	S = f1.readline()
	if S != '\n':
		print(r"'"+S.rstrip('\n')+r'\n'+r"'"+' '+'+'+'\n',file=f)
	else:
		print(r"'"+r'\n'+r"'"+' '+'+'+'\n',file=f)
f.close()