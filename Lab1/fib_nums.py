num1 = 1
num2 = 1
terms = 10
stage = 2

print(num1)
print(num2)

while(stage < terms):
	a = num1 + num2
	print (a)
	stage = stage + 1
	num1 = num2
	num2 = a


