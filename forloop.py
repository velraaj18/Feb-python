s= 'velraaj'
for i in s:     # iterate over each element of S with name i
   print(i)
   
dict1= dict({'name':'vel', 'age':21})
for i in dict1:
   print(i,dict1[i])  # i => key value of the dictionary

list1 = ['hello','world']
for i in list1:
   print(i)

for i in range(1, 4): 
	for j in range(1, 4): 
		print([i, j]) 
  
str1 = 'virat kohli'
for i in str1:
   if i=='a' or i=='l':
      continue
   print(f"letters: {i}") 

str2='rohit sharma'
i=0
while(i<len(str2)):
   if str2[i]=='m' or str2[i]=='a':
      i+=1
      continue
   print(f"letters: {str2[i]}")
   i+=1