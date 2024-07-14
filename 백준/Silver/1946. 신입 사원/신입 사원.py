import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    N = int(input())
    total = []
    for _ in range(N):
        a, b = map(int, input().split())
        total.append((a, b))

    total.sort(key=lambda x: x[0])
    cnt = 1
    check = total[0][1]
    for i in range(1, N):
        if total[i][1] < check:
            check = total[i][1]
            cnt += 1
    print(cnt)