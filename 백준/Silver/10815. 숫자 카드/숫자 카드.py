N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

_dict = {}
for i in range(len(arrN)):
  _dict[arrN[i]] = 0 

for j in range(M):
  if arrM[j] not in _dict:
    print(0, end=' ')
  else:
    print(1, end=' ')