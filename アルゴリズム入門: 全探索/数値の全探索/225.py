n = int(input())
FB = "FizzBuzz"
F = "Fizz"
B = "Buzz"
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(FB)
        continue
    if i % 3 == 0:
        print(F)
        continue
    if i % 5 == 0:
        print(B)
        continue
    print(i)
