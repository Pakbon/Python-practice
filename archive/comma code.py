zin=''
spam = ['apples', 'bananas', 'tofu', 'cats']
def comma(lijst):
	global zin
	n=0
	for items in lijst:
		n+=1
		zin = str(items) 
		if n != 3:
			print(zin +', ',end='')
			
		else:
			print(zin +' and ',end='')
comma(spam)