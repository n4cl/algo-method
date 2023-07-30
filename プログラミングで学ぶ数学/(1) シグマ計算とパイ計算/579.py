n = int(input())
a = list(map(int, input().split()))
ans = 1

for i in range(0, n):
    ans *= a[i]
print(str(ans)[-1])
