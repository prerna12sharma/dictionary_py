dic={1:20,2:10,3:30,4:40,5:50}
max=0
min=dic[1]
for i in dic:
    if dic[i]>max:
        max=dic[i]
    elif dic[i]<min:
        min=dic[i]
print(max,min)

