n = int(input())
ans = 0

for i in range(1, n):
    for j in range(i+1, n+1):
        ans = ans + i * j
print(ans)
