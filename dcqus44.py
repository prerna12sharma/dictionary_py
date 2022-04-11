d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
x={}
z=[]
c=[]
for i,j in d.items():
        if i=="Science":
            d[i]=d[i][0]
            c.append(d)
        if i=="Language":
            d[i]=d[i][0]
            c.append(d)
print(c)
# dict={}
# for i in d:
#     j=0
#     while j<len(d[i]):
#         list=[]
#         if i=="Science":
#             list.append(d[i][j])
#             dict[i]=list
#             # print(dict)
#         if i=="Language":
#             list.append(d[i][j])
#             dict[i]=list
#             print(dict)
#         j+=1
        

