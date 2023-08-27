import sys
sys.setrecursionlimit(2000)

def func(x):
    if x == 0:
        return 0
    else:
        return x + func(x-1)

print(func(int(input())))
