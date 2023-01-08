n = int(input())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(int(input()))]
cnt = [0] * 100001
for i in a:
    cnt[i] += 1

for j in x:
    print(cnt[j])
