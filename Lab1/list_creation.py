import math

lst = list()					#initially list is empty
lst.append(0.2)

print('1',lst[0])
for i in range(1,1000): 			
	num_temp = (lst[i-1] + math.pi)*100
	num_int = int(num_temp) 		#way to get something in int
	num_add = num_temp - num_int
	num_changed = num_add % 10000
	lst.append(num_changed)
	print (i+1,lst[i])
	
