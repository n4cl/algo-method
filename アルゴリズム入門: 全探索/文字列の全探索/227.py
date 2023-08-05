s = input()

for _s, _r in zip(s, reversed(s)):
    if _s != _r:
        print("No")
        exit()
print("Yes")
