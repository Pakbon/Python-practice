"""Vedic maths
calculate the square of a number ending with 5
Also used as an exercise in threading"""

import threading
import queue

nummer =0

def calculate(x):
	strnum=str(x)
	if strnum[-1] != '5':
		return 'number must end with 5'
	else:
		firstnum=int(strnum[:-1])
		scndnum=int(strnum[:-1])+1
		multiply=str(firstnum*scndnum)
		result=int(multiply+'25')
		return str(result)

while True:
	print('enter a number ending in 5')
	nummer=input()
	output=threading.Thread(target=calculate, args=[nummer])
	output.start()
	print(f'answer is {output}')