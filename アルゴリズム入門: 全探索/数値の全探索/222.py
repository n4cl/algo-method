n = int(input())

if n == 1:
    print("No")
    exit()

for i in range(2, n):
    if n % i == 0:
        print("No")
        exit()
print("Yes")
