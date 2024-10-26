def solution(wallet, bill):
    answer = 0
    
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        bill[bill.index(max(bill))] = int(bill[bill.index(max(bill))] / 2)
        answer += 1
    
    return answer