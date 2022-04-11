p="miisseetq"
c=[]
for i in p:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(set(c))
