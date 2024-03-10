a = int(input())
for i in range(a):
    x, y, z = map(int, input().split())
    if x == 1:
        print(x * y)
    else:
        print(x * y + (x-1) * z)
