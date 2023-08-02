def twoSum(array,target):
    array.sort()
    L = 0
    R = len(array)-1
    while(L<R):
        sum = array[L]+array[R]
        if(sum<target):
            L+=1
        elif(sum>target):
            R-=1
        elif(sum == target):
            return [array[L],array[R]]
    return []

array = [10,5,-5,3,6,7,8,-6,88,4]
target = 5
print(twoSum(array,target))