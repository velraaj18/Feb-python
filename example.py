class overload:
   def __init__(self,value):
      self.b= value              #initializes an attribute value
   def __add__(self,a):
      return(self.b+a.b)      # two instances of the class 

def main():
   obj1 =overload(2)
   obj2 =overload(3)
   print(obj2+obj1)
   print(overload.__add__(obj1,obj2))  #Operator overload => addition without + symbol.
   print(obj1.__add__(obj2))
if __name__ =="__main__":
   main()
   