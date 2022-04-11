d='w3resource'
count={}
for i in d:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

