h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] != t[i][j]:
            ans += 1

print(ans)
