N = int(input())
s = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(N):
  s += A[i]*B[i]

print(s)