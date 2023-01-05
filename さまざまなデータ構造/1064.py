h, w = map(int, input().split())
t = [input() for i in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if t[i][j] == "o":
            ans += 1

print(ans)
