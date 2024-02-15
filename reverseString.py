def fun():
   string1="Partha"
   print(string1[::-1])

def fun2():
   string2 = "partha"
   string2= list(string2)
   string2.reverse()
   reversedString = "".join(string2)
   print(reversedString)
   
def main():
   fun()
   print("\r")  #Creates a empty line of space.
   fun2()

if __name__ == "__main__":
   main()
   
