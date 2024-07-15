n, l = map(int, input().split())

apple = list(map(int, input().split()))
apple.sort()

for i in range(len(apple)):
  if apple[i] > l:
    break
  else:
    l += 1

print(l)