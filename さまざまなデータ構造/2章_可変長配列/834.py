input()
a = list(map(int, input().split()))
b = []

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        b.append(q[1])
    elif q[0] == 1:
        a.append(q[1])
    else:
        if len(b) > q[1]:
            print(b[-(q[1]+1)])
        else:
            qb = q[1] - len(b)
            if qb < len(a):
                print(a[qb])
            else:
                print("Error")
