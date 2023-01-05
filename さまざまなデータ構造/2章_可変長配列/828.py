input()
a = list(map(int, input().split()))

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        a.append(q[1])
    else:
        if len(a) > 0:
            print(a.pop(-1))
        else:
            print("Error")
