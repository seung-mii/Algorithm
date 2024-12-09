def solution(word):
    num = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(w, s):
        nonlocal num

        if s == w:
            return num
        
        if len(s) < 5:
            for d in dic:
                num += 1
                result = dfs(w, s + d)
                
                if result is not None:
                    return result
        
    return dfs(word, "")