import sys
input = sys.stdin.readline

n = int(input())
files = sorted(list(map(int, input().split())))

cnt = 0
for i in range(n):
  start, end = i, n-1
  
  while start <= end:
    mid = (start + end) // 2

    if files[i] >= 0.9 * files[mid]:
      start = mid + 1
    else:
      end = mid - 1
  
  cnt += start - i - 1
print(cnt)