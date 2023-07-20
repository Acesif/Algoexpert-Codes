def valid_parenthesis(s):
    stack = []
    closeToOpen = {")":"(","}":"{","]":"["}
    for i in s:
        if i in closeToOpen:
            if stack and stack[-1]==closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False
s = "()[]{}"
print(valid_parenthesis(s))
