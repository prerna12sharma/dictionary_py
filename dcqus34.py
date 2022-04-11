d={'key1': 1, 'key2': 3, 'key3': 2}
dic={'key1': 1, 'key2': 2}
c=0
for i in d.items():
    for j in dic.items():
        if i in dic.items():
            c=c+1
            print(i)
            break
print(c)
