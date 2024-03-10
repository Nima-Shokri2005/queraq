my_list = list(map(int, input().split()))
n = 5
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x = my_list[i]
            y = my_list[j]
            z = my_list[k]
            if x + y > z and x + z > y and z + y > x:
                print("YES")
                exit(0)
print("NO")
