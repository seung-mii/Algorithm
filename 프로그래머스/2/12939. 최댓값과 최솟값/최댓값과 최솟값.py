def solution(s):
    answer = ''
    ary = list(map(int, s.split()))
    answer += str(min(ary)) + ' '
    answer += str(max(ary))
    return answer