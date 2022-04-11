d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
y=[]
b=[]
r=[]
c={}
for i,j in d:
    if i=="yellow":
        y.append(j)
        c[i]=y
    if i=="blue":
        b.append(j)
        c[i]=b
    if i=="red":
        r.append(j)
        c[i]=r
print(c)
