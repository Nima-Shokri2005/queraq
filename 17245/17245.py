T = ["*****", "oo*oo", "oo*oo"]
A = ["oo*oo", "o***o", "*ooo*"]
X = ["*ooo*", "oo*oo", "*ooo*"]
M = ["**o**", "*o*o*", "*ooo*"]
N = ["*ooo*", "*o*o*", "*ooo*"]
a1 = input()
a2 = input()
a3 = input()
q = 0
w = 0
m1 = [[]]
m2 = [[]]
m3 = [[]]
t1 = []
t2 = []
t3 = []
for i in range(len(a1)):
    t1.append(a1[i])
    t2.append(a2[i])
    t3.append(a3[i])
    if (i + 1) % 5 == 0:
        m1.append(t1)
        m2.append(t2)
        m3.append(t3)
        t1 = []
        t2 = []
        t3 = []
m1.pop(0)
m2.pop(0)
m3.pop(0)
for i in range(len(m1)):
    if ''.join(m1[i]) == ''.join(T[0]) and ''.join(m2[i]) == ''.join(T[1]) and ''.join(m3[i]) == ''.join(T[2]):
        print("T", end="")
    if ''.join(m1[i]) == ''.join(A[0]) and ''.join(m2[i]) == ''.join(A[1]) and ''.join(m3[i]) == ''.join(A[2]):
        print("A", end="")
    if ''.join(m1[i]) == ''.join(X[0]) and ''.join(m2[i]) == ''.join(X[1]) and ''.join(m3[i]) == ''.join(X[2]):
        print("X", end="")
    if ''.join(m1[i]) == ''.join(M[0]) and ''.join(m2[i]) == ''.join(M[1]) and ''.join(m3[i]) == ''.join(M[2]):
        print("M", end="")
    if ''.join(m1[i]) == ''.join(N[0]) and ''.join(m2[i]) == ''.join(N[1]) and ''.join(m3[i]) == ''.join(N[2]):
        print("N", end="")
