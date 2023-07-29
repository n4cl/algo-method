l, r = map(int, input().split())
ans = 0

for i in range(l, r+1):
    ans = ans + (2*i-1)**2
print(ans)
