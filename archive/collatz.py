def collatz(number):
	if number % 2 == 0:
		even=number // 2
		print(even)
	elif number %2 == 1:
		odd=number * 3 + 1
		print(odd)

print('enter a number')
n=int(input())
collatz(n)