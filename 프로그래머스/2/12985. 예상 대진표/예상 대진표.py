def solution(n,a,b):
    answer = 0
    a -= 1
    b -= 1
    ary = []
    
    for i in range(n):
        ary.append(i) 
    
    while True:
        temp = []
        answer += 1
        for i in range(0, len(ary), 2): 
            if (ary[i] != a and ary[i+1] != a and ary[i] != b and ary[i+1] != b) or (ary[i] == a or ary[i] == b):
                temp.append(ary[i])
            if ary[i+1] == a or ary[i+1] == b:
                temp.append(ary[i+1])
            if (ary[i] == a and ary[i+1] == b) or (ary[i] == b and ary[i+1] == a):
                return answer
        ary = temp