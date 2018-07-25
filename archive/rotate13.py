#rotate 13
#take a string
#loop through string, skip space, ignore leestekens
#rotate 13, store in variable
#output answer

def rotate(zinput):
	zinrotated=''
	alphabet='abcdefghijklmnopqrstuvwxyz'
	for l in zinput:
		if l.isalpha()==False:
			zinrotated+=str(l)
			continue
		positie=alphabet.index(l)
		rotate=positie-13
		zinrotated+=alphabet[rotate]
	return zinrotated

def main():
	userinput=input('Rotate13\nEnter a string\n')
	#check=userinput.isalpha()
	#if check==True:
	answer=rotate(userinput.lower())
	print(answer)
	#else:
	#	print('Only alphanumeric characters')
			
main()