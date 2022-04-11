# d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# list=[]
# for i in d:
#     s={}
#     for j in i:
#         a=int(i[j])
#         s[j]=a
#     list.append(s)
# print(list)

d=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
list=[]
for i in d:
    s={}
    for j in i:
        a=float(i[j])
        s[j]=a
    list.append(s)
print(list)
