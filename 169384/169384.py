a = int(input())
for i in range(a):
    b = input()
    sum = 0
    for j in range (len(b)):
        if b[j]=='>':
            sum += len(b)-1-j
        if b[j]=='<':
            sum += j
    print(sum)