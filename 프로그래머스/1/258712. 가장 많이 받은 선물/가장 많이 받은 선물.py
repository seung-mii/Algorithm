def solution(friends, gifts):
    people = [[0] * len(friends) for _ in range(len(friends))]
    cnt = {} # 선물 지수
    gift = [0] * len(friends) # 받는 선물 수
    
    for f in friends:
        cnt[f] = 0
    
    for g in gifts:
        give, receive = g.split()
        people[friends.index(give)][friends.index(receive)] += 1
        cnt[give] += 1
        cnt[receive] -= 1
    
    for i in range(len(people)):
        for j in range(len(people)):
            if people[i][j] > people[j][i]:
                gift[i] += 1
            elif people[i][j] < people[j][i]:
                gift[j] += 1
            else:
                if cnt[friends[i]] > cnt[friends[j]]:
                    gift[i] += 1
                elif cnt[friends[i]] < cnt[friends[j]]:
                    gift[j] += 1
                    
    return max(gift) // 2