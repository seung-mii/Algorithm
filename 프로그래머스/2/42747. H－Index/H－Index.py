def solution(citations):
    citations.sort(reverse=True)

    for i in range(max(citations), -1, -1): # 2
        count = 0
        for c in citations:  # 3
            if c >= i: 
                count += 1 # 1
            if count >= i:
                return i