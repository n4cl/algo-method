h, w, x, y = map(int, input().split())
x -= 1
y -= 1
t = [input() for i in range(h)]
for i in range(h):
    s = ""
    for j in range(w):
        if x <= i and i < (x + 3):
            if y <= j and j < (y + 3):
                s += t[i][j]
    if s: print(s)
