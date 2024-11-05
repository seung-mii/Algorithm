def solution(n):
    ary = [0, 1, 1, 2]
    
    for i in range(4, n+1):
        ary.append(ary[i-1] + ary[i-2])

    return (ary[n] % 1234567)