n = input()
s = input()
t = input()
ans = 0
for _s, _t in zip(s, t):
    if _s != _t:
        ans += 1
print(ans)
