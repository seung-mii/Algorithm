def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else: 
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
    
    if len(stack) == 0:
        return True
    else:
        return False