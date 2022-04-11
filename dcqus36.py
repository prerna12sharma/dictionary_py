d={'c1': 'Red', 'c2': 'Green', 'c3': None}
s={}
for (i, j) in d.items():
    if j==None:
        pass
    else:
        s[i]=j
print(s)

