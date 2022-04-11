d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic={}
for i in d.values():
    j=0
    while j<=len(i):
        dic[i]=j
        j=j+1
print(dic)