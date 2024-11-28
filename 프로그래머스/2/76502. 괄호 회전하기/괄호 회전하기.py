def solution(s):
    answer = 0
    arys = []
    for value in s:
        arys.append(value)
    
    for i in range(len(arys)):
        stack = []
        for item in arys:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            if item == ')':
                if ('(' not in stack) or stack[-1] != '(':
                    stack.append(item)
                    break
                else:
                    stack.pop()
            if item == ']':
                if ('[' not in stack) or stack[-1] != '[':
                    stack.append(item)
                    break
                else:
                    stack.pop()
            if item == '}':
                if ('{' not in stack) or stack[-1] != '{':
                    stack.append(item)
                    break
                else:
                    stack.pop()
        
        if len(stack) == 0:
            answer += 1
        
        temp = arys.pop(0)
        arys.append(temp)
    
    return answer