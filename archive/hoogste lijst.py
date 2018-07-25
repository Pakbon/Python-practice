elements=('hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen')
hoogste='element'
lengte=0
for i in elements:
	if lengte > len(i):
		continue
	else:
		lengte=len(i)
		hoogste=i
print(hoogste +', ' + str(lengte) + ' characters')