d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
smax=0
thmax=0
m=0
s=0
t=0
l=[]
li=[]
lis=[]
for i in d.keys():
    list=[]
    if d[i]>max:
        thmax=smax
        t=s
        smax=max
        s=m
        max=d[i]
        m=i
        l.append(m)
        print('first highest value',l)
        break   
    if d[i] !=max and d[i]>smax:
        thmax=smax
        t=s
        smax=d[i]
        s=i
        li.append(m)
        li.append(s)
        break
    print('second highest value',li)
    if d[i]!=max and d[i] !=smax and d[i]>thmax:
        thmax=d[i]
        t=i
        lis.append(m)
        lis.append(s)
        lis.append(t)
        break
    print('third highest value',lis)
list.append(lis)
print(list)

