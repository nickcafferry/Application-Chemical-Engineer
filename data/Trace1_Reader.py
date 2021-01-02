#!/usr/local/bin/python

output0 = open("rention_time.txt", 'w', encoding="utf-8")
output1 = open("intensity.txt", 'w', encoding="utf-8")

length = len(open('Trace1.csv','r', encoding='utf-8').readlines())

with open('Trace1.csv', 'r', encoding='utf-8') as f:
	for i in range(length):
		line = f.readline()
		print('[%s, %s]'%(line.split()[1].strip(','), line.split()[2].strip('\n')), end=',', file=output0)
	
output0.close()

with open('Trace1.csv', 'r', encoding='utf-8') as f:
	for i in range(length):
		print(f.readline().split(',')[2].strip('\n'), end=',', file=output1)
	
output1.close()