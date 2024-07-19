import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
day = 1

tree.sort()

for i in range(1, n):
  day += 1
  tree[i] -= i

tree.sort(reverse=True)
day += tree[0] + 1
print(day)