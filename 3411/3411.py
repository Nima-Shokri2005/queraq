def count_factors_of_5_in_factorial(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count


a = int(input())
count = count_factors_of_5_in_factorial(a)
flag = True
c = 0
u = 1
for i in range(1, a + 1):
    while flag and count!=0:
        if i % 2 != 0:
            break
        else:
            i //= 2
            c += 1
        if c == count:
            flag = False
    if i%5==0:
        while True:
            if i%5==0:
                i //= 5
            else:
                break
    u = str(u)
    i = str(i)
    x = int(u[len(u)-1])*int(i[len(i)-1])
    u = int(u)
    u = x
u = str(u)
print(u[len(u)-1])