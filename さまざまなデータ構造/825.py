l = [3,1,4,1,5,9,2,6,5,3]
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 0:
        print(l[q[1]])
    else:
        l[q[1]] = q[2]
