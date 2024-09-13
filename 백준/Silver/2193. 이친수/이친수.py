n = int(input())
cnt = [1, 1, 2]

for i in range(3, n):
  cnt.append(cnt[i-1] + cnt[i-2])

print(cnt[n-1])