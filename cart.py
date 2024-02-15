class items:
   food =2000
   ice=1000
   def cart(self):
      return(self.food+self.ice)

def main():
   obj1 = items()
   print(obj1.cart())

if __name__ == "__main__":
   main()
      