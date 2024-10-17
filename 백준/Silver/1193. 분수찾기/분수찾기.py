x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    child = x
    parents = line - x + 1
else:
    child = line - x + 1
    parents = x

print(child, '/', parents, sep='')