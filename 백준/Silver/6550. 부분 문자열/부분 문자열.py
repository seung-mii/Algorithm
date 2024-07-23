while True:
  try:
    s,t = map(str, input().split())
    list_s = list(map(str, s))
    index = 0

    for i in range(len(t)):
      if index == len(s):
        break

      if s[index] == t[i]:
        index += 1

    print("Yes" if len(s) == index else "No")
  except:
      break