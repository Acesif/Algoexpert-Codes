s = "anagram"
t = "aganram"
def validateAnagram(s,t):
    if(len(s) == len(t)):
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT
    else:
        return False

print(validateAnagram(s,t))