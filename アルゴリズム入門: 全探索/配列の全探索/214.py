n = int(input())
a = list(map(int, input().split()))
min_a = 101

for i, a_i in enumerate(a):
    if min_a > a_i:
        min_a = a_i

print(min_a)
