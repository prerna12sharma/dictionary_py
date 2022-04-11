d=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], 
[3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# di={}
# for i in d:
#     d=[]
#     for j in i:
#         if j==0:
#             di[i][j]=d
#         else:
#             d.append(d[i])
#             di[j]=d
# print(di)
di={}
i=0
while i<len(d):
    j=0
    c=0
    lis=[]
    while j<len(d[i]):
        if j==0:
            c=d[i][j]
        else:
            lis.append(d[i][j])
        j=j+1
    di[c]=lis
    i=i+1
print(di)            


















