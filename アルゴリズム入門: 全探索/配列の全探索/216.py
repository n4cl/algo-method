def main():
    n, v = map(int, input().split())
    a = list(map(int, input().split()))
    p = -1
    for i in range(len(a)):
        if v == a[i]:
            p = i
    return p

print(main())
