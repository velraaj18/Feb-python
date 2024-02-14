class operator:
   def __init__(self,a,b):  #here self is not a parameter.It provides the instance for the other parameters of the class
      self.a =a
      self.b=b
   def __add__(self,other):  #Here self is also a parameter.
      return self.a+other.a, self.b+other.b
def main():
  obj1=operator(3,4)
  obj2=operator(5,6)
  print(obj1+obj2)      #Operator overloading
  print(obj1.__add__(obj2))
  print(operator.__add__(obj2,obj2))
if __name__ == "__main__":
   main()