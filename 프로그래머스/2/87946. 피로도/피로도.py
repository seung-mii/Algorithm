def solution(k, dungeons):
    max_count = 0
    visited = [False] * len(dungeons)

    def dfs(k, count):
        nonlocal max_count
        max_count = max(max_count, count)

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)
    return max_count
