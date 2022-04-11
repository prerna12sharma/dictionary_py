dict={1:20,2:10}
a={}
dic=list(dict.values())
dic.sort()
for i in dic:
    for j in dict:
        if i==dict[j]:
            a[j]=i
print(a)
print(dic)