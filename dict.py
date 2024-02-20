dict1 = {"name":"velraaj", "age": 21}
dict2 = dict({"name" : "Virat", "age" : 35})

dict1.update(dict2)    #don't support duplicate keys. the most recent key gets updated.

print(dict1)