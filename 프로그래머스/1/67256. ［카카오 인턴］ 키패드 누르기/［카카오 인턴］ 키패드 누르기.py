def solution(numbers, hand):
    answer = ''
    cur = [[0, 3], [2, 3]] 
    hand = 'R' if hand == 'right' else 'L' 
    
    for n in numbers:
        if n in [1, 4, 7]: 
            answer += 'L'
            cur[0] = [(n - 1) % 3, (n - 1) // 3]
        elif n in [3, 6, 9]: 
            answer += 'R'
            cur[1] = [(n - 1) % 3, (n - 1) // 3]
        else: 
            target = [(n - 1) % 3 if n != 0 else 1, (n - 1) // 3 if n != 0 else 3]
            left_length = abs(cur[0][0] - target[0]) + abs(cur[0][1] - target[1])
            right_length = abs(cur[1][0] - target[0]) + abs(cur[1][1] - target[1])

            if left_length == right_length:
                answer += hand
                cur[0 if hand == 'L' else 1] = target
            elif left_length < right_length:
                answer += 'L'
                cur[0] = target
            else:
                answer += 'R'
                cur[1] = target

    return answer
