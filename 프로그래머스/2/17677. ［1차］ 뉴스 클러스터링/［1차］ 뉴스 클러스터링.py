from collections import Counter

def solution(str1, str2):
    def make_pairs(s):
        return [s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()]

    counter1 = Counter(make_pairs(str1))
    counter2 = Counter(make_pairs(str2))
    
    intersection = counter1 & counter2
    union = counter1 | counter2

    inter_size = sum(intersection.values())
    union_size = sum(union.values())

    return int((inter_size / union_size) * 65536) if union_size != 0 else 65536