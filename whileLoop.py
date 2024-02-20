# Program to print except m and a
str2='rohit sharma'
i=0
while(i<len(str2)):
   if str2[i]=='m' or str2[i]=='a':
      i+=1
      continue
   print(f"letters: {str2[i]}")
   i+=1

# Program to quit when entering 6
a= int(input('enter the number(6 to quit):'))
while a!=6:
   a= int(input('enter the number(6 to quit):'))
   
counter = 10
while counter>0:
   print(counter)
   counter-=1
print('Blast off')
   