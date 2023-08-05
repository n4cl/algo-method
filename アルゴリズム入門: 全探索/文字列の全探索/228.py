s = input()
ans = 0
_temp = ""
for _s in s:
    if _s == _temp:
        ans += 1
    _temp = _s
print(ans)
