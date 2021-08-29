n, x, y = map(int, input().split())

for i in range(n-2):
    x, y = y, (x+y) % 100

print(y)
