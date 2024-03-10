import math

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    m = abs(a * b) // math.gcd(a, b)
    x = math.log2(m // a)
    if x == math.floor(x):
        print(int(x))
    else:
        print(-1)
