N = int(input())
result = 0

time = []
time = list(map(int, input().split()))
time.sort()
result += time[0] 

for i in range(1, N) :
  # 각 사람이 기다리는 시간의 총합은 정렬된 리스트의 처음부터 현재 사람까지의 합
  result += sum(time[:i + 1])

print(result)