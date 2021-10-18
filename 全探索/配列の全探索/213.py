def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = -100
    for val in a:
        if t < val:
            t = val
    return t

print(main())
