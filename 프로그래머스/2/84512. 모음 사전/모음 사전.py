def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0

    for i, char in enumerate(word):
        index = vowels.index(char)
        
        for j in range(5 - i):
            answer += index * (5 ** j)
            
        answer += 1 

    return answer