d={'S   001': ['Math', 'Science'], 'S   002': ['Math', 'English']}
s={}
for i,j in d.items():
    for k in " ":
        i=i.replace(k,"")
        s[i]=j
print(s)
