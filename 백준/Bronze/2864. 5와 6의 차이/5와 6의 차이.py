a, b = map(str, input().split())

min_a = a.replace('6', '5')
max_a = a.replace('5', '6')

min_b = b.replace('6', '5')
max_b = b.replace('5', '6')

print((int(min_a) + int(min_b)), (int(max_a) + int(max_b)))