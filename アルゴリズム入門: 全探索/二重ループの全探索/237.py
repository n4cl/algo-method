n = int(input())
ans = 0

def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True

for _ in range(n):
    if is_palindrome(input()):
        ans += 1

print(ans)
