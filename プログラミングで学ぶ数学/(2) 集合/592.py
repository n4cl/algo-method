n, x = map(int, input().split())
ans = 0
for i in range(1, n+1):
    if i % x == 0:
        ans += 1
print(ans)
