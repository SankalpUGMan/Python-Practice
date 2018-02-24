with open("ques3_doc", "r") as f:	 #opens file for reading in string format
	contents = f.read()	  

words = contents.split()	 	 #breaking the string in words form

d = {}				 	 #creating an empty dictionary/array for storage and checking

for i in words:				 #i is a string now
		i = i.lower() 		 #lowers down all capitals (an optional step)
		if i in d:		 #if the word is in our dictionary, we are incrementing the counter
			d[i] += 1
		else:			 #else, we are just adding the word in our dictionary with a counter
			d[i] = 1
for j in d:
	print('%s : %d'% (j, d[j]))	 #nice publishing tech. 
	#print(j, d[j])			 #python 2.7.6 publishes in brackets form. for publishing in python 3, do python3 file_manipulation.py. python 3 has no brackets


	

