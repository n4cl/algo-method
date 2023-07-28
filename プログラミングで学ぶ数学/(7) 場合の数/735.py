n = input()
a = set(map(int, input().split()))
ans = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i in a or j in a or k in a:
                ans += 1
print(ans)
