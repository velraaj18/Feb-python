def armstrong(number):
   number_str= str(number)
   n= len(number_str)
   sum=0
   for i in number_str:
      sum+=int(i)**n
   if sum == number:
         print("armstrong")
   else:
         print("not a armstrong")
      
def main():
  result = armstrong(100)
  print(result)

if __name__ =="__main__":
   main()