s = input()
target = "UCPC"
idx = 0

for char in s:
    if char == target[idx]:
        idx += 1
        if idx == len(target):
            print("I love UCPC")
            break
else:
    print("I hate UCPC")