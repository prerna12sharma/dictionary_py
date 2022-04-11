d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
count={}
for  i in d1.keys():
    for j in d2.keys():
        if i==j: 
            count[i]=d1[i]+d2[j]
else:
    count[i]=d1[i]
    count[j]=d2[j]
print(count)