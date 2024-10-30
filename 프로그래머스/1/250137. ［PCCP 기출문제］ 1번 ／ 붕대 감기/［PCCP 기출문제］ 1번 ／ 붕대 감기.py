def solution(bandage, health, attacks):
    cur_health = health
    count = 0
    
    for i in range(1, attacks[len(attacks)-1][0]+1):
        # 공격 여부
        if i != attacks[0][0]:
            count += 1 # 1
            
                
            # 연속 성공
            if count == bandage[0]:
                cur_health += bandage[2]
                count = 0
            
            # 체력 회복
            cur_health += bandage[1] # 5
            if cur_health > health:
                cur_health = health
            
        else:
            cur_health -= attacks[0][1]
            count = 0
            attacks.pop(0)
        
        # 사망
        if cur_health <= 0:
            cur_health = -1
            break
            
    return cur_health