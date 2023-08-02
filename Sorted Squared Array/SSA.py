def sortedSqArr(array):
    sqArr = [0]*len(array)
    start = 0
    end = len(array)-1
    for idx in reversed(range(len(array))):
        smallVal = array[start]
        largeVal = array[end]
        if(abs(smallVal)<abs(largeVal)):
            sqArr[idx] = array[end]**2
            end-=1
        else:
            sqArr[idx] = array[start]**2
            start+=1
    return sqArr

li = [-7,-5,-4,3,6,8,9]
print(sortedSqArr(li))