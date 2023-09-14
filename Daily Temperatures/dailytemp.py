# Input: 
temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
def daily_temp(temp):
    res = [0]*len(temperatures)
    stack = [] # [idx,temp]
    for idx,temp in enumerate(temperatures):
        while stack and temp>stack[-1][1]:
            stackIdx,stackTemp = stack.pop()
            res[stackIdx] = (idx - stackIdx)
        stack.append([idx,temp])
    return res

print(daily_temp(temperatures))        
