n = int(input())
student = list(map(int, input().split()))
student.sort()
group = []

for i in range(n):
  group.append(student[i] + student[len(student)-i-1])

print(min(group))