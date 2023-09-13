n, k = list(map(int, input().split()))
ans = 0


def get_divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


for j in range(1, n+1):
    if get_divisor(j) == k:
        ans += 1

print(ans)
