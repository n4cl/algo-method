n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_set = set()
b_set = set()
for i in range(0, n):
    a_set.add(a[i])
for j in range(0, m):
    b_set.add(b[j])
ans = list(a_set.intersection(b_set))
ans.sort()
for i in ans:
    print(i)
