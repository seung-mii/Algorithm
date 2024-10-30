def solution(players, callings):
    dic = {p: i for i, p in enumerate(players)}

    for c in callings:
        cur = dic[c]
        pre = cur - 1

        players[cur], players[pre] = players[pre], players[cur]

        dic[players[cur]] = cur
        dic[players[pre]] = pre

    return players