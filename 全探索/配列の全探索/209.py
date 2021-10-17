n, v = map(int, input().split())
a = list(map(int, input().split()))

def main():
    for val in a:
        if v == val:
            return "Yes"
    return "No"

print(main())
