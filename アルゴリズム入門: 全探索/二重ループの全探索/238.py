l, r = list(map(int, input().split()))
ans = 0


def is_palindrome(n):
    n = str(n)
    index = len(n)//2
    if index == 0:
        return True
    elif n[:index] == n[-index:]:
        return True
    return False

for j in range(l, r+1):
    if is_palindrome(j):
        ans += 1

print(ans)
