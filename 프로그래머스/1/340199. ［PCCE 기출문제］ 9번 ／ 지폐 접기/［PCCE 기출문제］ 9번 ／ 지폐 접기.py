def solution(wallet, bill):
    answer = 0
    
    while True:
        if max(bill) > max(wallet) or min(bill) > min(wallet):
            bill[bill.index(max(bill))] = int(bill[bill.index(max(bill))] / 2)
            answer += 1
        elif max(bill) <= max(wallet) and min(bill) <= min(wallet):
            break
    
    return answer