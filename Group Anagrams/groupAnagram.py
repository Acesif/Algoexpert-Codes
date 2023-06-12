from collections import defaultdict
def groupAnagram(str):
    result = defaultdict(list)
    for s in str:
        key = [0]*26
        for i in s:
            key[ord(i)-ord("a")]+=1
        result[tuple(key)].append(s)
    return result.values()

strs=['eat','tea','tan','ate','nat','bat']
print(groupAnagram(strs))