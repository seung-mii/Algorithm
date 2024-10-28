def solution(s, skip, index):
    answer = ''
    
    for i in s:
        cur = i
        count = 0 
        
        while count < index:
            if ord(cur) + 1 > 122: 
                cur = 'a'
            else:
                cur = chr(ord(cur) + 1)

            if cur not in skip:
                count += 1

        answer += cur 

    return answer
