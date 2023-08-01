n, x, y = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

s = set(i for i in range(1, n+1))
s -= a
s -= b
print(len(s))
