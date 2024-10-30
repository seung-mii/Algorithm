def solution(park, routes):
    h, w = len(park), len(park[0])
    dn = ['N', 'S', 'W', 'E']
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    graph = [[0] * w for _ in range(h)]
    cur_x, cur_y = 0, 0
    
    for i, par in enumerate(park):
        for j, p in enumerate(par): 
            if p == 'X': 
                graph[i][j] = 1
            if p == 'S':
                cur_x, cur_y = i, j

    for r in routes:
        t_x, t_y = cur_x, cur_y 
        for _ in range(int(r[2])):
            dx, dy = cur_x + d[dn.index(r[0])][0], cur_y + d[dn.index(r[0])][1]

            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] != 1:
                cur_x, cur_y = dx, dy
            else:
                cur_x, cur_y = t_x, t_y
                break 

    return [cur_x, cur_y]
