n = int(input())
a = list(map(int, input().split()))

c = [0] * 10 * 10 ** 5

for i in a:
    c[i] += 1

ans = 0
mx = 0
for j, v in enumerate(c):
    if mx < v:
        mx = v
        ans = j

print(ans)

