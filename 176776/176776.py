str = input()
str += "1"
my_list = list()
score = 0
for i in str:
    if i == "0":
        score += 1
    if i == "1":
        my_list.append(score)
        score = 0
print(max(my_list))