n, v = map(int, input().split())
a = list(map(int, input().split()))

def main():
    cnt = 0
    for val in a:
        if v == val:
            cnt += 1
    return cnt

print(main())
