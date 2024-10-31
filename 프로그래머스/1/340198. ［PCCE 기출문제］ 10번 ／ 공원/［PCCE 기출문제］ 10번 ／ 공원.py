def solution(mats, park):
    mats.sort(reverse=True)
    h, w = len(park), len(park[0])

    for mat_size in mats:
        for i in range(h - mat_size + 1):
            for j in range(w - mat_size + 1):
                can_place = True
                for k in range(mat_size):
                    for l in range(mat_size):
                        if park[i + k][j + l] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    return mat_size

    return -1
