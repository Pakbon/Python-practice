'''trying out generators and their uses'''

from time import sleep

def generator(num):
    for i in range(num):
        yield i ** 3

def textgen(text):
    for i in text:
        yield i * 2

for num in generator(8):
    print(num)

for t in textgen('testing'):
    print(t,end='')
