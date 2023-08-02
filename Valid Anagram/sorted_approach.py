s = "anagram"
t = "aganram"
def validateAnagram(s,t):
    return sorted([*s])==sorted([*t])
print(validateAnagram(s,t))