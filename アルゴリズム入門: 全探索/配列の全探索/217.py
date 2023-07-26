n = int(input())
a = list(map(int, input().split()))
b = [0] * 10
for a_i in a:
    b[a_i] += 1

for b_i in b[1:]:
    print(b_i)
