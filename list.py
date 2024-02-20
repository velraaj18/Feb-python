list1 = [1,5]
result = list((i,list1[i]) for i in range(len(list1)))   # to return the index of the respective values
print(result)

def list2(r1,r2):
    return [ i for i in range(r1,r2+1)]    # => return List[(i for i in range(r1,r2+1))]
result2=list2(1,5)
print(result2)

list3 = [1,4,3,9,4,0]
print(sorted(list3))
print(sorted(set(list3)))