import sys
input = sys.stdin.readline

n, m = map(int, input().split())
power = []

for i in range(n):
  a, b = input().split()
  power.append([a, int(b)])

for j in range(m):
  char = int(input())
  start, end = 0, len(power) - 1

  while start <= end:
    mid = (start+end) // 2

    if char > power[mid][1]:
      start = mid + 1
    else:
      end = mid - 1

  print(power[start][0])