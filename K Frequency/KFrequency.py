nums = [1,1,1,2,2,2,3]
k = 2

def topKFrequncy(nums,k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n,c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        for j in freq[i]:
            res.append(j)
            if len(res) == k:
                return res

print(topKFrequncy(nums,k))