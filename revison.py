# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# dic={}
# for i in d1.keys():
#     for j in d2.keys():
#         if i==j:
#             dic[i]=d1[i]+d2[j]
# else:
#     dic[i]=d1[i]
#     dic[j]=d2[j]
#print(dic)


# d='w3resource'
# s={}
# for i in d:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(s)

# d=dict()
# for i in range(1,6):
#     d[i]=i**2
# print(d)

# d={0: 10, 1: 20}
# d[2]=30
# print(d)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict={}
# dict.update(dic1)
# dict.update(dic2)
# dict.update(dic3)
# print(dict)

# d={"name":"riya","age":20}
# user=input("enter")
# if user in d:
#     print("yes,key in dic")
# else:
#     print("no")

# d={1:2,2:3,3:4,4:5,5:6}
# sum=0
# for i in d.values():
#     sum=sum+i
# print(sum)

# d={1:2,2:3,3:4,4:5,5:6}
# mul=1
# for i in d.values():
#     mul=mul*i
# print(mul)

# d={1:2,2:3,3:4,4:5,5:6}
# d.pop(1)
# print(d)

# d=["rash","kil","varsha"]
# di=[1,2,3]
# res={}
# for i in d:
#     for j in di:
#         res[i]=j
#         di.remove(j)
#         break
# print(res)

# d={1:6,2:3,3:4,4:5,5:7}
# max=0
# min=d[1]
# for i in d:
#     if d[i]>max:
#         max=d[i]
#     elif d[i]<min:
#         min=d[i]
#print(max,min)

# d={'id1':{'name':['Sara'],'class':['V'],'subject_integration':['english,math,science']},
#  'id2':{'name': ['David'],'class':['V'],'subject_integration':['english, math, science']},
#  'id3':{'name': ['Sara'],'class': ['V'],'subject_integration':['english,math,science']},
#  'id4':{'name':['Surya'],'class':['V'],'subject_integration':['english, math, science']}}
# res={}
# for i,j in d.items():
#     if j not in res.values():
#         res[i]=j
# print(res)

# d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#  {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# res=[]
# for i in d: 
#     for j in i.values():
#         if j not in res:
#             res.append(j) 
# print(set(res))

# d= {'1':['a','b'], '2':['c','d']}
# res={}
# for i in d['1']:
#     for j in d['2']:
#         res=i+j
#         print(res)


# d={1:6,2:3,3:4,4:5,5:7}
# max=0
# smax=0
# thmax=0
# m=0
# s=0
# t=0
# for i in d.keys():
#     if d[i]>max:
#         thmax=smax
#         t=s
#         smax=max
#         s=m
#         max=d[i]
#         m=i
#     elif d[i]>smax:
#         thmax=smax
#         t=s
#         smax=d[i]
#         s=i
#     elif d[i]>thmax:
#         thmax=d[i]
#         t=i
# print(max,smax,thmax)
# print(m,s,t)

# d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
#   {'item': 'item1', 'amount': 750}]
# s={}
# for i in d:
#     if i['item'] not in s:
#         s[i['item']]=i['amount']
#     else:
#         s[i['item']]+=i['amount']
# print(s)
#dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# d = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# sum=0
# val=0
# for i in d:
#     sum=sum+i['id']
#     val=val+i['success']
# print(sum)
# print(val)

# list= [1, 2, 3, 4]
# d=res={}
# for i in list:
#     res[i]={}
#     res=res[i]
# print(d)

# dic={'a':8,'b':2,'c':3}
# for i in sorted(dic):
#     print(i,dic[i])

# d='iloveindia'
# s=()
# for i in d:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(s)

# d= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# c=0
# for i in d:
#     c=c+1
#     print(i,d[i],c)

# d={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'v','roll_id':3}} 
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j,':',d[i][j])                                                                                                     

# d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in d:
#     for j in d[i]:
#         c=c+1
# print(c)

# d={'key1': 1, 'key2': 3, 'key3': 2}
# di= {'key1': 1, 'key2': 2}
# c=0
# for i in d.items():
#     for j in di.items():
#         if i in di.items():
#             print(i)
#             c=c+1
#             break
# print(c)


# d={ 'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#     'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#     'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in d:
#     j=0
#     while j<len(d[i]):
#         if j==4:
#             print(d[i][j])
#         j=j+1

# d=["rekha","pinki","rani"]
# f=[2,5,6]
# res={}
# for i in d:
#     for j in f:
#         res[i]=j
#         f.remove(j)
#         break
# print(res)

d=[10,20,3,4,5,6,7,8]
res={}
g=[]
li=[]
i=1
while i<len(d):
    g.append(i)
    if i==3:
        res['c1']=g
        break
    i=i+1
print(res)

# d=[1,2,3,4,5,6,7,8,9,10]
# list=["c1","c2","c3","c4"]
# dict={}
# g=[]
# count=1
# i=0
# while i<len(d):
#     g.append(d[i])
#     if count==3:
#         dict[i]=g
#         g=[]
#         count=0
#     count+=1
#     i=i+1d=[1,2,3,4,5,6,7,8,9,10]
dict={}
g=[]
e=['c1','c2','c3']
count=1
i=0
j=0
while i<len(d):
    g.append(i)
    for j in e:
        # if count==3:
            dict[j]=g
    if count==3:            
        g=[]
        count=0
        count+=1
        break
    i=i+1
print(dict)
# print(dict)
    
    
    
        