from collections import Counter

n = int(input())
c = Counter(list(map(int, input().split())))
print(c.most_common()[0][0])
