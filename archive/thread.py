"""threading and queue practice
Create a FIFO queue, write data to it
from one thread. Read data from another
thread
20180725"""

import queue,threading,time


#initiate queue,set variables
Q_obj=queue.Queue(maxsize=6)
lijst=['1','2','3','a','b','c'] #sample data
c=0 #counter to stop while loop in main()

#initiate and start thread. Prints data from thread 
def main(): 
	global c
	thrd_obj=threading.Thread(target=newthr, args=(lijst,)) #create thread, pass arguments
	thrd_obj.start()
	while True:
		result=Q_obj.get()
		print(result)
		time.sleep(1)
		c+=1
		if c == 6:
			break


def newthr(x):
	data_obj=''
	for i in x:
		data_obj=i#something to data_obj
		Q_obj.put(data_obj)

main()
