n = input()
a = list(map(int, input().split()))
ans = 0


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for a_i in a:
    if is_prime(a_i):
        ans += 1

print(ans)
