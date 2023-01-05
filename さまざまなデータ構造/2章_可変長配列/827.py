input()
a = list(map(int, input().split()))

for _ in range(int(input())):
    q, v = list(map(int, input().split()))
    if q == 0:
        if len(a) > v:
            print(a[v])
        else:
            print("Error")
    else:
        a.append(v)
