class Animal:
    att1 = "Dog"
    att2 = "Cat"
    def fun(self):
        print("First animal is : ", self.att1)
        print("Second animal is : " , self.att2)

def main():
    Animal1 = Animal()
    print(Animal1.att1)
    Animal1.fun()

if __name__ == "__main__":
    main()
        