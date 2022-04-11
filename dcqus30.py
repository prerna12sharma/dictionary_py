d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
smax=0
thmax=0
for i in d.keys():
    if d[i]>max:
        thmax=smax
        smax=max
        max=d[i]  
    elif d[i]>smax:
        thmax=smax 
        smax=d[i]
    elif d[i]>thmax:
        thmax=d[i]
print(max,smax,thmax) 