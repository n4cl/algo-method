n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a = a - b
a = list(a)
a.sort()
for a_i in a:
    print(a_i)
