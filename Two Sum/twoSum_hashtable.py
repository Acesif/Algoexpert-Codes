def twoSum(array,target):
    hashtable = {}
    for x in array:
        y = target - x
        if(y in hashtable):
            return [x,y]
        else:
            hashtable[x] = True
    return []

array = [10,5,-5,3,6,7,8,-6,88,4]
target = 5
print(twoSum(array,target))