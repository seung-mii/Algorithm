N = int(input())
meetings = []
result = 0

for i in range(N):
  start, end = map(int, input().split())
  meetings.append((end, start))

meetings.sort()
end_time = 0

for meeting in meetings:
  if meeting[1] >= end_time:
    result += 1
    end_time = meeting[0]

print(result)