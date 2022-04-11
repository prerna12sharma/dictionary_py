student=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
#print(sum(i['id'] for i in student))
#print(sum(i['success'] for i in student))
sum=0
val=0
for i in student:
    sum=sum+i['id']
    val=val+i['success']
print(sum)
print(val)


 


