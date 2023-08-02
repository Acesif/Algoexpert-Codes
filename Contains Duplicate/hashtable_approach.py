def containsDup(array):
    hash = {}
    for i in array:
        if i in hash:
            return True
        else:
            hash[i] = True
    return False

array = [1,2,5,6,3]
print(containsDup(array))