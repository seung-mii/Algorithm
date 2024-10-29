def solution(numbers, hand):
    answer = ''
    cur = [[0, 3], [2, 3]]  # 0 2 1 3
    
    for n in numbers: # 8
        if n == 1 or n == 4 or n == 7:
            answer += 'L' 
            cur[0][0] = (n-1) % 3 # 0 
            cur[0][1] = (n-1) // 3 # 2
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            cur[1][0] = (n-1) % 3
            cur[1][1] = (n-1) // 3
        elif n == 2 or n == 5 or n == 8:
            left_length = abs(cur[0][0] - ((n-1) % 3)) + abs(cur[0][1] - ((n-1) // 3))  # 1 + 0 = 1
            right_length = abs(cur[1][0] - ((n-1) % 3)) + abs(cur[1][1] - ((n-1) // 3)) # 0 + 1 = 1 

            if left_length == right_length:
                if hand == 'right':
                    answer += 'R'
                    cur[1] = [(n-1) % 3, (n-1) // 3]
                else:
                    answer += 'L'
                    cur[0] = [(n-1) % 3, (n-1) // 3]
            elif left_length < right_length:
                answer += 'L'
                cur[0] = [(n-1) % 3, (n-1) // 3]
            else:
                answer += 'R'
                cur[1] = [(n-1) % 3, (n-1) // 3]
        else: # n == 0
            left_length = abs(cur[0][0] - 1) + abs(cur[0][1] - 3)  # 1 + 1 = 2
            right_length = abs(cur[1][0] - 1) + abs(cur[1][1] - 3) # 1 + 0 = 1

            if left_length == right_length:
                if hand == 'right':
                    answer += 'R'
                    cur[1] = [1, 3]
                else:
                    answer += 'L'
                    cur[0] = [1, 3]
            elif left_length < right_length:
                answer += 'L'
                cur[0] = [1, 3]
            else:
                answer += 'R'
                cur[1] = [1, 3]
            
    
    return answer