import math
n = int(input())
for i in range(n):
    r, w, l = map(int, input().split())
    x = math.sqrt(w*w+l*l)
    if x<=2*r:
        print("Pizza fits on the table.")
    else:
        print("Pizza does not fit on the table.")