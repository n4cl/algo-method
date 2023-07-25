n = int(input())
a = list(map(int, input().split()))
max_a = 0
ans = 0
for i, a_i in enumerate(a):
    if max_a < a_i:
        max_a = a_i
        ans = i

print(ans)
