from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    answer = participant_count - completion_count  
    return list(answer.keys())[0]  
