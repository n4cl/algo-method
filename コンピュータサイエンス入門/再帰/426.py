import sys
sys.setrecursionlimit(10**6)

def func(x, y):
    if x == y:
        return x
    else:
        return x + func(x+1, y)

a, b = map(int, input().split())
print(func(a, b))
