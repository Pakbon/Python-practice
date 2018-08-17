import os, re, subprocess, datetime

dt=datetime.date.today()
dt=dt.strftime("%Y-%m-%d")
curdir=os.getcwd()
logfile='{}/{}.log'.format(curdir, dt)
grepfile='{}/{}.grep'.format(curdir, dt)
uinput='/var/log/auth.log'
nmap_args=['/usr/bin/nmap', '-iL', logfile, '-n', '-F', '-sV','--version-light', '-oG', grepfile]


def main():
	'pass data around, call nmap'
	found=findIP()
	logging(found)
	nmap=subprocess.Popen(nmap_args)

def logging(text):
	with open(logfile, 'w') as log:
		for i in text:
			log.write(i)
			log.write('\n')

def findIP():
	lijst=[]
	reg= re.compile(r'\d+\.\d+\.\d+\.\d+(?<!Accepted)') #find all ipaddresses, except for lines saying 'accepted'
	with open(uinput) as file:
		results=reg.findall(file.read()) 
		results.sort()
		for i in results: #duplicate filter
			if i not in lijst:
				lijst+=[i]
	return lijst

if __name__=='__main__':
	main()
