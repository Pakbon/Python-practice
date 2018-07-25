import os
import re

def bestand(file, n, text):
	if n == 'openen':
		inputfile= open(file)
		findIP(file)
		inputfile.close()
	else:
		logwrite=open(logfile,'a')
		logwrite.write(text)
		logwrite.write('\n')
		logwrite.close()

def findIP(textfile):
	iplist=open(textfile)
	iplistread=iplist.read()
	reg= re.compile(r'\d+\.\d+\.\d+\.\d+')
	results=reg.findall(iplistread)
	results.sort()
	for i in results:
		bestand('', 'log', i)
		print(i)

print('open an file')
userinput=os.path.join(input())
logfile=userinput+'.log'
bestand(userinput, 'openen','')
input('press enter to continue')