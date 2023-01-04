input()
a = list(map(int, input().split()))
a.reverse()

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        a.append(q[1])
    else:
        print(a.pop()) if a else print("Error")
