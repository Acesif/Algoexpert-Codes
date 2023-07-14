# Problem: Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode.

# Example
# Input: [“lint”,“code”,“love”,“you”]
# Output: [“lint”,“code”,“love”,“you”]
# Explanation: One possible encode method is: “lint:;code:;love:;you”

# Example
# Input: [“we”, “say”, ":", “yes”]
# Output: [“we”, “say”, ":", “yes”]
# Explanation: One possible encode method is: “we:;say:;:::;yes”

def en_str(strs):
    res = ""
    for i in strs:
        res += str(len(i)) + "#" + i
    return res

def de_str(str):
    res,i = [],0
    while i<len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j+1:j+1+length])
        i = j+1+length
    return res

in_en = ["we","say",":","yes"]
encoded = en_str(in_en)
print(in_en)
print(de_str(encoded))