a = int(input())
my_list = list(map(int, input().split()))
my_list.sort()
for i in range (len(my_list)):
    if (my_list[i]!=0):
        sum1 = my_list[i]
        sum2 = my_list[i]
        index = i
        break
    else:
        sum1 = 0
        sum2 = 0
        index = 0
for i in range(index+1,len(my_list)):
    if i%2==0:
        sum1 += my_list[i]
        sum2 -= my_list[i]
    if i%2==1:
        sum1 -= my_list[i]
        sum2 += my_list[i]
print(min(abs(sum1),abs(sum2)))