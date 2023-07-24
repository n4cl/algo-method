x = int(input())
a = list(map(int, input().split()))
coins = [50, 10, 5, 1]
ans = 0

for _c, _a in zip(coins, a):
    min_a = min(x // _c, _a)
    if min_a == 0:
        continue
    x = x - min_a * _c
    ans += min_a

print(ans)
