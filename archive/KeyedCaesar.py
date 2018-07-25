"""Cipher implementation of Keyed Caesar
based on http://rumkin.com/tools/cipher/
Purely for practice purposes"""

def main():
	tekst=str(input('Enter text to transform\n'))
	keyword=str(input('Enter a keyword\n'))
	rotate=int(input('Enter amount to rotate\n'))
	getkey=keying(keyword)
	print(rotating(tekst,rotate,getkey))
	
def keying(keyword):
	alphabet=('abcdefghijklmnopqrstuvwxyz')
	#create keyed alphabet
	kwlength=len(keyword)
	keyed=keyword+alphabet[kwlength:]
	return keyed
	
def rotating(tekst,rotate,getkey):
	zinrotated=''
	for l in tekst:
		if l.isalpha()==False:
			zinrotated+=str(l)
			continue
		positie=getkey.index(l)
		rotation=positie-rotate
		zinrotated+=getkey[rotation]
	return zinrotated
	
main()