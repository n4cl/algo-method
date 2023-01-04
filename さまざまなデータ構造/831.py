input()
a = list(map(int, input().split()))

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        a.reverse()
    elif q[0] == 1:
        a.append(q[1])
    else:
        print(a.pop(-1)) if a else print("Error")
