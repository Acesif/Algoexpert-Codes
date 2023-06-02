def containsDup(array):
    return len(array)!=len(set(array))
array = [1,2,5,6,3,1]
print(containsDup(array))