import sys
input = sys.stdin.readline

def bs(start, end, note1, i):
    while start <= end: 
      mid = (start + end) // 2
      
      if note1[mid] == note2[i]: 
        return 1 
      elif note1[mid] > note2[i]:
        end = mid - 1
      else:
        start = mid + 1
    return 0 

for _ in range(int(input())):
    n = int(input())
    note1 = sorted(list(map(int,input().split())))
    m = int(input())
    note2 = list(map(int,input().split())) 

    for i in range(m):
      print(bs(0, n-1, note1, i)) 