import sys
input = sys.stdin.readline

n = int(input())
line = []
tip = 0

for i in range(n):
  line.append(int(input()))

line.sort(reverse=True)

for i in range(n):
  if line[i]-(i+1-1) > 0:
    tip += line[i]-(i+1-1)

print(tip)