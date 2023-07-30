n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = set()
for i in range(0, n):
    s.add(a[i])
for j in range(0, m):
    s.add(b[j])
ans = list(s)
ans.sort()
for i in ans:
    print(i)
