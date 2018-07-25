"""fibonacci up till number
2018-07-24"""
a=0
b=1
n=input('enter a number for fibonacci range: ')
if n.isdecimal():
    n=(int(n)//2)
    for i in range(1,n):
        a+=b
        print(a,end=', ')
        b+=a
        print(b,end=', ')