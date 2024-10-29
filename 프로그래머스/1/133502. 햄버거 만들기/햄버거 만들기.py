def solution(ingredient):
    answer = 0  
    stack = []

    for i in ingredient:
        if i != 1 and len(stack) == 0:
            continue
        else: 
            stack.append(i)

            if stack[-4:] == [1, 2, 3, 1]:
                answer += 1 
                stack.pop(len(stack)-1)
                stack.pop(len(stack)-1)
                stack.pop(len(stack)-1)
                stack.pop(len(stack)-1)

    return answer
