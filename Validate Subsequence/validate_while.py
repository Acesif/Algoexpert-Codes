def subseq(array,subseq):
    seqIdx = 0
    arrIdx = 0
    while(seqIdx<len(subseq) and arrIdx<len(array)):
        if(subseq[seqIdx] == array[arrIdx]):
            seqIdx+=1
        arrIdx +=1
    return seqIdx == len(subseq)

arr=[1,2,5,88,641,1,2,3]
sub=[1,1,3]
print(subseq(arr,sub))
