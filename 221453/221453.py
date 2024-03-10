n, V = map(int, input().split())
fruits = []
for _ in range(n):
    h, v = map(int, input().split())
    fruits.append((h, v))
fruits.sort(key=lambda x: x[0] / x[1], reverse=True)
total_happiness = 0.0
for h, v in fruits:
    if V >= v:
        total_happiness += h
        V -= v
    else:
        total_happiness += (V / v) * h
        break
print("{:.1f}".format(total_happiness))
