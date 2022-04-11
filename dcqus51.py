d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic={}
for i,j in d.items():
    o=[]
    for k in j:
        if k%2==0:
            o.append(k)
            d[i]=o
print(d)
# d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# dic={}
# for i,j in d.items():
#     o=[]
#     for k in j:
#         if k%2!=0:
#             d[i].clear()
#         else:
#             o.append(k)
#             d[i]=o
# print(d)
    