a = int(input())
if a==1:
    print(0)
    exit(0)
l = 0
for i in range(1,a):
    if a%i==0:
        l += i
y = 0
u = 0
while True:
    if y==l:
        print(1)
        break
    if y>i:
        print(0)
        break
    else:
        y = pow(2,u)
        u += 1