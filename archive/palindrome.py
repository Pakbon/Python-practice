#reverse a string


def reverser(string,lengte):
	n=0
	reverse=''
	for letter in string:
		n-=1
		reverse=reverse + string[n]
	return reverse
	
def comparison(oristring,revstring):
	if oristring == revstring: 
		return 1
	else:
		return 0
	

def main():
	message=str(input('type a sentence '))
	#messagelength=0
	messagelength=len(message)
	revresult=''
	revresult=reverser(message,messagelength)
	print('reversed string is:' + revresult)
	compareresult=comparison(message, revresult)
	if compareresult==1:
		print('Palindrome')
	else:
		print('Not a palindrome')

main()