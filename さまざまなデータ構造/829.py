input()
a = list(map(int, input().split()))

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        a.insert(q[1], q[2])
    elif q[0] == 1:
        a.pop(q[1])
    else:
        print(a.count(q[1]))
