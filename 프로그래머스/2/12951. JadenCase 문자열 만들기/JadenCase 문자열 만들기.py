def solution(s):
    ary = s.split(" ")
    
    for i, a in enumerate(ary):
        if a == "":
            continue
        else: 
            ary[i] = a[0].upper() + a[1:].lower()
        
    return ' '.join(ary)