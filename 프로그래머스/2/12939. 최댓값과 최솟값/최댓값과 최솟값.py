def solution(s):
    ary = list(map(int, s.split()))
    return str(min(ary)) + ' ' + str(max(ary))