d=[{'id': '#FF0000', 'color': 'Red'},
 {'id': '#800000', 'color': 'Maroon'},
 {'id': '#FFFF00', 'color': 'Yellow'}, 
{'id': '#808000', 'color': 'Olive'}]
s=[]
for i in d:
    if i['id'] !='#FF0000':
        s.append(i)
print(s)