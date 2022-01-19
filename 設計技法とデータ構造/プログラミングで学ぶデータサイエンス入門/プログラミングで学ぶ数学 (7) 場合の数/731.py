x, y = map(int, input().split())
ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        _sum = i + j
        if _sum == x or _sum == y:
            ans += 1
print(ans)
