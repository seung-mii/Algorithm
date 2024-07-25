k, n = map(int, input().split())
lan = sorted([int(input()) for _ in range(k)])
left, right = 1, max(lan)

while left <= right:
  mid = (left + right) // 2
  length = 0

  for i in range(k):
    length += (lan[i] // mid)
  
  if length < n:
    right = mid - 1
  else:
    left = mid + 1

print(right)