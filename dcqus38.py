d=['S001', 'S002', 'S003', 'S004']
di=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
dic=[85, 98, 89, 92]
a=[]
for i in d:
    b={}
    for j in di:
        c={}
        for k in dic:
            c[j]=k
            b[i]=c
            a.append(b)
            dic.remove(k)
            break
        di.remove(j)
        break
print(a)
