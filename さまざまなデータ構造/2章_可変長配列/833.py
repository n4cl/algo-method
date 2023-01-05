n = int(input())
a = [i+1 for i in range(n)]
ans = 0
while True:
    if len(a) == 1:
        ans = a[0]
        break
    a.pop(0)
    a.append(a[0])
    a.pop(0)

print(ans)

