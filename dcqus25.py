dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# s=[]
# for i in dict['C1']:
#     for j in (dict['C2']):
#         for k in (dict['C3']):
#             s.append(i)
#             s.append(j)
#             s.append(k)
#             #print(dict[i,j,k],end='')
# print(s)
print(*list(dict.keys()))
a=(list(dict.values()))
for i in range(len(a)):
    print(*a([i]))