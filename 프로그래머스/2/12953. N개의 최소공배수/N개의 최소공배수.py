import math

def solution(arr):
    answer = arr[0]
    
    for a in arr:
        answer = abs(answer * a) // math.gcd(answer, a)

    return answer