import re

result = re.search('velraaj' , "My name is velraaj")
print(result)
print(result.group())  #Gives the search OP
print(result.start())  #Starting index
print(result.end())    #Last index