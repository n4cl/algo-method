def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    tmp = a[0]
    for i in range(1, len(a)):
        if tmp < a[i]:
            cnt += 1
        tmp = a[i]

    return cnt

print(main())
