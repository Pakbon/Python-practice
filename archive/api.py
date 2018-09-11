'''using https://jsonplaceholder.typicode.com/posts/ as input,
take command argument of 'userId',
print all 'title'\n'body' '''
import sys,json,requests

def main():
	#runs through program
	#take arguments from command line (sys.argv)
	print('type a number')
	uinput=input()
	data=fetch()
	proc(data, uinput)

def fetch():
	#fetch website and their answer
	link='https://jsonplaceholder.typicode.com/posts/'
	res=requests.get(link)
	if res.status_code == 200:
		answer=res.content
		#take res variable
		#return to main
		return answer
	#else:
		#request failed
		##return back to user
		
def proc(data,uinput):
	dictio=json.loads(data)
	for i in dictio:
		user=int(i['userId'])
		if user == int(uinput):
			print('\ntitle: ' + i['title']+ '\n' +i['body'] + '\n')
	print('finished')

main()
