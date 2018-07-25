'''Fizzbuzz
Type 'Fizz' for any number dividable by 3
Type 'Buzz' for any number dividable by 5
Type 'FizzBuzz for numbers dividable by both'''


for i in range(1,101):
	fb=''
	if i%3 == 0:
		#fizzable
		fb+='Fizz'
	if i%5 == 0:
		#buzzable
		fb+='Buzz'
	if fb == '':
		print(i)
	else:
		print(fb)